# Hospital Management System

A Django-based educational hospital-management application with separate administrative, doctor and patient experiences. Features in the source include doctor and patient registration, approval workflows, appointment management and discharge invoices.

> **Not for real patient records or clinical operations.** This repository is a learning/demo application and has not undergone a healthcare compliance or production security audit.

## Security notes

The original version exposed public administrator registration. The registration view now returns **403 Forbidden**. Create trusted administrators out-of-band using Django's `createsuperuser` command; review group-based authorization before real-world deployment. The existing committed SQLite database and historical settings may contain sensitive information. **Inspect them and rotate any real credentials; modifying current files does not erase Git history.** Do not commit private patient data.

The development key is intentionally insecure. Set a strong unique `DJANGO_SECRET_KEY` before deployment. Keep `DJANGO_DEBUG=false` and configure `DJANGO_ALLOWED_HOSTS`. Configure HTTPS, secure cookies, logging, backups and permission reviews before any deployment.

## Local setup

Install Python 3.11 or 3.12 and create a virtual environment:

```bash
git clone https://github.com/DemonJ01/Hospital-Management.git
cd Hospital-Management
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # optional reference only; Django reads shell environment variables
export DJANGO_DEBUG=true
export DJANGO_SECRET_KEY=replace-with-a-random-local-development-key
python -m django check
python -m django migrate
python -m django createsuperuser
python -m django runserver
```

On Windows PowerShell use `$env:DJANGO_DEBUG="true"` and `$env:DJANGO_SECRET_KEY="..."` instead of `export`. **The repository has no tracked manage.py** as of this repair; Django commands above require a project entry point. This repair supplies a standard `manage.py` in the repository root.

Open http://127.0.0.1:8000/ locally. Use a dedicated local test database rather than real patient records.

## Project layout

- `hospital/`: models, forms, views, and database migrations.
- `hospitalmanagement/`: primary Django project settings, routes and WSGI/ASGI.
- `projectname/`: secondary/legacy Django project configuration (retained for compatibility; review before deleting).
- `templates/hospital/`: HTML templates.
- `static/`: CSS, UI assets and screenshots.
- `manage.py`: primary Django entry point.

## Configuration

See `.env.example`. Django reads environment variables from the process; it **does not automatically load a .env file**. Configure them in your shell or process manager. Email integration requires valid provider credentials. Google's obsolete "less secure apps" setup is **not supported**; use an approved application password or another supported SMTP provider.

## Validation

```bash
python -m compileall -q hospital hospitalmanagement projectname manage.py
python -m django check
python -m django test
```

End-to-end functionality and security of all user journeys are **not verified** by these checks. Review account approval permissions, invoice access, destructive endpoints and personally identifiable information handling before deployment.

## Known limitations

- A SQLite database and Python cache artifacts remain in existing Git history. This repair does not delete historical data.
- Security hardening is partial; administrative route and individual object-level authorization require a fuller audit.
- The duplicated secondary Django project configuration needs manual confirmation before removal.
- Image uploads and email require environment-specific setup.
