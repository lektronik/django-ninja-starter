# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

**Do not open a public issue.** Instead, email: **telis.aslanidis.io@gmail.com**

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact

You will receive a response within 48 hours.

## Security Defaults

This boilerplate ships with production security hardening that activates automatically when `DEBUG=False`:

- **CSRF Protection** — Secure CSRF cookies in production
- **Session Security** — Secure, HTTP-only session cookies
- **HSTS** — Strict Transport Security with 1-year max-age and preload
- **SSL Redirect** — Automatic HTTP → HTTPS redirect
- **CORS** — Restrictive origin policy (allowlist-only in production)
- **Password Validation** — Full Django password validator chain enabled

## Environment Variables

Never commit secrets to the repository. Use the `.env` file (excluded from git via `.gitignore`) for:

- `SECRET_KEY` — Django secret key (generate a unique one for production)
- `DEBUG` — Set to `False` in production
- `ALLOWED_HOSTS` — Comma-separated list of allowed hostnames

## Dependencies

Dependencies are pinned in `requirements.txt` to prevent supply chain attacks. Regularly audit with:

```bash
pip audit
```
