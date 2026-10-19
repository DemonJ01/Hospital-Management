# Contributing to Hospital-Management

This is a Django educational project, **not suitable for production clinical use**.

1. Create a feature branch and read [the architecture](docs/ARCHITECTURE.md).
2. Set up a virtual environment and dependencies as explained in README.
3. Never use real patient records or production credentials in test fixtures.
4. Run `python manage.py check`, `python manage.py test`, and compile checks.
5. Submit reviewable pull requests explaining security impacts and remaining gaps.

Changes to authorization or medical records require object-level access tests. Do not remove existing database files or change historical migrations without careful review of effects and backups.

The repository license remains unspecified.
