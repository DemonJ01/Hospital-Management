# Security policy — Hospital-Management

This educational application has **not** passed a complete security audit and must not be used with real medical data.

## High-priority concerns

- The repository includes a tracked SQLite database and Python compiled caches; both may contain sensitive material. Inspect and sanitize carefully. `.gitignore` cannot erase Git history.
- Older commits contain hardcoded Django configuration. Rotate any real credentials before deployment.
- Public admin registration is blocked on the repair branch, but authorization across all routes remains incompletely audited.
- Invoice access has an additional ownership guard; test other endpoints for horizontal privilege escalation, especially modifying/deleting patient records.
- Verify CSRF, HTTPS, session handling, object-level permissions, deployment settings and SMTP credentials.

## Reporting

Avoid public security details. Contact an administrator privately or use private vulnerability reporting if enabled. No response-time guarantee has been established.
