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
