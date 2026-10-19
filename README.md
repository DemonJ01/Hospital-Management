# Hospital-Management

Educational Django hospital workflow prototype with administrator, doctor and patient roles.

**Current scope:** Python, Django, SQLite, Django templates, CSS, django-widget-tweaks, xhtml2pdf.

> Please review the [known limitations](docs/KNOWN_LIMITATIONS.md) before using or presenting this project. Documentation describes the implementation actually available in this repository; additional functionality is not implied.

## Project quick start

Clone the repository, change into its directory, then execute:

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export DJANGO_DEBUG=true
export DJANGO_SECRET_KEY=local-development-only-change-this
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
~~~

The examples target a Unix-like shell. On Windows, activate the virtual environment with the Windows script and configure environment variables using PowerShell syntax where applicable.

## Validation

~~~bash
python -m compileall -q hospital hospitalmanagement projectname manage.py
python manage.py check
python manage.py test
~~~

Checks require the relevant Python/Node.js dependencies and, for some functionality, external services. Continuous integration may cover a smaller subset than full manual runtime validation. See the [technical architecture guide](docs/ARCHITECTURE.md) and [test strategy](docs/TESTING.md).

## What is implemented

`hospitalmanagement/` holds the active Django project configuration and URLs. `hospital/` contains models, forms, views and historical migrations. HTML templates and `static/` provide the UI. SQLite stores application data locally. `projectname/` is retained legacy Django configuration with unverified purpose. Admin signup and invoice downloads have received targeted guards; this is not an exhaustive authorization review.

## Known limitations

An SQLite database and compiled Python artifacts are already in Git history; .gitignore does not erase them. Do not use real health data or deploy for clinical care. Other destructive and object-level operations need thorough authorization tests. SMTP depends on a configured provider. Legacy project configuration requires review.

For more information, see [docs/KNOWN_LIMITATIONS.md](docs/KNOWN_LIMITATIONS.md).

## Project documentation

- [Architecture](docs/ARCHITECTURE.md) — components and data flow.
- [Testing](docs/TESTING.md) — checks, limits and manual verification.
- [Known limitations](docs/KNOWN_LIMITATIONS.md) — outstanding risks and missing features.
- [Contributing](CONTRIBUTING.md) — local development and pull request guidelines.
- [Security](SECURITY.md) — privacy and vulnerability reporting guidance.

## Contribution and license

Please contribute through a feature branch and a reviewable pull request. Never add secrets, private data or unverifiable feature claims to commits. A repository-wide license has not been selected in this improvement pass; ownership and third-party licensing must be reviewed before publishing one.

