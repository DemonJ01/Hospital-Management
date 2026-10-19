# Architecture — Hospital-Management

`hospitalmanagement/` holds the active Django project configuration and URLs. `hospital/` contains models, forms, views and historical migrations. HTML templates and `static/` provide the UI. SQLite stores application data locally. `projectname/` is retained legacy Django configuration with unverified purpose. Admin signup and invoice downloads have received targeted guards; this is not an exhaustive authorization review.

## Technology

Python, Django, SQLite, Django templates, CSS, django-widget-tweaks, xhtml2pdf.

## Trust boundaries and dependencies

An SQLite database and compiled Python artifacts are already in Git history; .gitignore does not erase them. Do not use real health data or deploy for clinical care. Other destructive and object-level operations need thorough authorization tests. SMTP depends on a configured provider. Legacy project configuration requires review.

Changes to external services, persistence, authentication, model inference or exchange integrations should include tests for failure cases, error handling and authorization rather than relying only on compilation.
