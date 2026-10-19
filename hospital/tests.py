from django.contrib.auth.models import Group, User
from django.test import TestCase, override_settings
from django.urls import reverse
from hospital.models import Patient, Appointment


class AuthorizationRegressionTests(TestCase):
    def test_public_admin_enrollment_is_blocked(self):
        self.assertEqual(self.client.get('/adminsignup').status_code, 403)

    def test_patient_search_requires_login(self):
        self.assertEqual(self.client.get('/searchdoctor').status_code, 302)

    def test_doctor_directory_requires_login(self):
        self.assertEqual(self.client.get('/patient-view-doctor').status_code, 302)

    def test_unauthenticated_invoice_redirects(self):
        self.assertEqual(self.client.get('/download-pdf/1').status_code, 302)

    def test_doctor_self_signup_does_not_grant_approval(self):
        data = {'first_name': 'Test', 'last_name': 'Doctor', 'username': 'testdoctor', 'password': 'secure-Test1', 'address': 'Sample', 'mobile': '5550000000', 'department': 'Cardiologist'}
        response = self.client.post('/doctorsignup', data)
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='testdoctor')
        self.assertFalse(user.doctor.status)

    def test_doctor_cannot_delete_another_doctors_appointment(self):
        from hospital.models import Doctor
        current = User.objects.create_user('doctor_current', password='example-Test123')
        other = User.objects.create_user('doctor_other', password='example-Test123')
        group, _ = Group.objects.get_or_create(name='DOCTOR')
        current.groups.add(group)
        Doctor.objects.create(user=current, address='Test', status=True)
        Doctor.objects.create(user=other, address='Test', status=True)
        appointment = Appointment.objects.create(doctorId=other.id, patientId=123, description='test')
        self.client.force_login(current)
        self.assertEqual(self.client.get(f'/delete-appointment/{appointment.id}').status_code, 404)
        self.assertTrue(Appointment.objects.filter(pk=appointment.pk).exists())


class TemplateSmokeTests(TestCase):
    """The public entry points must render without missing templates."""

    def test_public_pages_render(self):
        for url in ('/', '/doctorclick', '/patientclick', '/doctorlogin', '/patientlogin', '/doctorsignup', '/patientsignup', '/contactus'):
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_login_pages_contain_csrf(self):
        for url in ('/doctorlogin', '/patientlogin'):
            with self.subTest(url=url):
                self.assertContains(self.client.get(url), 'csrfmiddlewaretoken')


class AppointmentAndSearchRegressionTests(TestCase):
    def test_search_without_query_redirects_anonymous_user(self):
        self.assertEqual(self.client.get('/searchdoctor').status_code, 302)

    def test_admin_appointment_uses_validated_doctor_and_patient(self):
        from hospital.models import Doctor, Patient
        admin = User.objects.create_user('admin_test', password='example-Test123')
        admin.groups.add(Group.objects.get_or_create(name='ADMIN')[0])
        doctor_user = User.objects.create_user('doctor_test', first_name='Doctor', password='example-Test123')
        patient_user = User.objects.create_user('patient_test', first_name='Patient', password='example-Test123')
        Doctor.objects.create(user=doctor_user, address='Ward', status=True)
        Patient.objects.create(user=patient_user, address='Ward', mobile='12345', symptoms='Checkup', status=True)
        self.client.force_login(admin)
        response = self.client.post('/admin-add-appointment', {
            'doctorId': str(doctor_user.id), 'patientId': str(patient_user.id),
            'description': 'Follow-up', 'status': 'on',
        })
        self.assertEqual(response.status_code, 302)
        appointment = Appointment.objects.get()
        self.assertEqual(appointment.doctorId, doctor_user.id)
        self.assertEqual(appointment.patientId, patient_user.id)


class SuperuserAccessTests(TestCase):
    def test_superuser_has_administrator_access_without_admin_group(self):
        superuser = User.objects.create_superuser('chief_admin', 'chief@example.invalid', 'secure-Test123')
        self.client.force_login(superuser)
        self.assertEqual(self.client.get('/admin-dashboard').status_code, 200)


class PostOnlyMutationTests(TestCase):
    def test_approval_and_deletion_routes_reject_get(self):
        admin = User.objects.create_superuser('workflow_admin', 'admin@example.invalid', 'secure-Test123')
        self.client.force_login(admin)
        urls = ['/approve-doctor/1', '/reject-doctor/1', '/approve-patient/1',
                '/reject-patient/1', '/approve-appointment/1', '/reject-appointment/1',
                '/delete-doctor-from-hospital/1', '/delete-patient-from-hospital/1']
        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 405)
