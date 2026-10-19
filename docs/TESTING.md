# Validation guide — Hospital-Management

## Commands

From the repository root, after installation:

~~~bash
python -m compileall -q hospital hospitalmanagement projectname manage.py
python manage.py check
python manage.py test
~~~

## Beyond static checks

An SQLite database and compiled Python artifacts are already in Git history; .gitignore does not erase them. Do not use real health data or deploy for clinical care. Other destructive and object-level operations need thorough authorization tests. SMTP depends on a configured provider. Legacy project configuration requires review.

Report which checks you actually ran; passing them does not prove all features work or that the app is production-secure. Record exact reproduction instructions and the environment for failures.

## Pull request review checklist

- [ ] New tests exercise changed behavior and relevant edge cases.
- [ ] Manual verification is described honestly.
- [ ] External services, secrets and missing files are documented.
- [ ] No unrelated changes or data files are committed.
