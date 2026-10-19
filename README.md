# Hospital Management System

A Django web application for managing hospital administration, doctors, patients, appointments, and discharge bills.

## Features
- Administrator, doctor, and patient roles.
- Doctor registration and approval.
- Patient registration, admission, and management.
- Appointment booking and approval.
- Patient discharge records and invoice generation.
- Separate dashboards for different user roles.

## Technologies
Python, Django, SQLite, HTML, CSS, Django templates, and xhtml2pdf.

## Installation
Use Python 3.11 or a compatible version.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate`.

## Configuration
Set the following environment variables for local development:

```bash
export DJANGO_DEBUG=true
export DJANGO_SECRET_KEY=replace-with-a-random-development-key
```

For deployment, set `DJANGO_DEBUG=false`, a unique `DJANGO_SECRET_KEY`, and `DJANGO_ALLOWED_HOSTS` to the actual domain or host.

## Run
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open the server address shown in the terminal. Use Django's admin account for initial setup.

## Tests
```bash
python manage.py check
python manage.py test hospital
```

## Project Structure
```text
hospital/           Models, forms, views, migrations and tests
hospitalmanagement/ Django settings and URL routes
templates/hospital/ Web page templates
static/             Stylesheets and images
manage.py           Django management entry point
```

**Note:** This is a demonstration application. Do not use real patient data without completing a production security and privacy review.
