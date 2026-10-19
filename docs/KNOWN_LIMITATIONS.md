# Known limitations — Hospital-Management

An SQLite database and compiled Python artifacts are already in Git history; .gitignore does not erase them. Do not use real health data or deploy for clinical care. Other destructive and object-level operations need thorough authorization tests. SMTP depends on a configured provider. Legacy project configuration requires review.

## Release readiness checklist

- [ ] All needed source and assets exist with appropriate usage rights.
- [ ] Credentials are supplied securely outside version control.
- [ ] Setup and deployment instructions work on a clean machine.
- [ ] CI checks and meaningful application tests pass.
- [ ] Security and data-privacy reviews are complete.
- [ ] Relevant dependencies and licenses have been audited.
- [ ] Screenshots, feature statements and benchmarks reflect verified behavior.

This file is an engineering inventory and does not certify production readiness.
