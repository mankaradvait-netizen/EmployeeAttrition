# Security Policy

## Reporting Vulnerabilities
If you discover a security vulnerability or security risk in this repository, please report it privately to the repository maintainers rather than opening a public issue.

## Security Guidelines for HR Data Analysis
- **Data Anonymization**: Ensure all HR employee datasets contain only anonymized or synthetic data, without direct Personally Identifiable Information (PII) such as SSNs or personal contacts.
- **Secrets Management**: Never commit API keys, Kaggle tokens, cloud credentials, or environment secrets to source control.
- **Execution Safety**: Keep Python dependencies updated and verify data processing scripts against unexpected code execution risks.
