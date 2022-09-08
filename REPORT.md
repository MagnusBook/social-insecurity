# Report

## OWASP Top 10
### A01:2021-Broken Access Control

### A02:2021-Cryptographic Failures

### A03:2021-Injection

### A04:2021-Insecure Design

### A05:2021-Security Misconfiguration

### A06:2021-Vulnerable and Outdated Components
Updated all Python packages used by Social Insecurity to latest versions. These updates include, but not limited to, using the latest version of Python and a new major version upgrade of Flask.

Un-maintained packages used by the application were replaced with maintained alternatives.

Packages included, but not needed by the application, were removed from the dependencies list. This includes the dependency `wincertstore` which could be used by an attacker to read the host's certificates.

### A07:2021-Identification and Authentication Failures

### A08:2021-Software and Data Integrity Failures

### A09:2021-Security Logging and Monitoring Failures

### A10:2021-Server-Side Request Forgery

## Comments

- No prepared statements used
- No Access control, does not check if user should have access (login)
- Deprecated dependencies
- Secret key not set.
- Deprecated: wincertstore support python up to version 3.4
- JQuery version
- Bootstrap version
