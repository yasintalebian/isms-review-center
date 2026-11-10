# Test server integration contract

This document is the checklist for connecting the dashboard to the test Linux server. No live connection is attempted by the initial scaffold.

## Required details

- Hostname/IP and SSH/SFTP or HTTPS transport.
- Port and authentication method (SSH key, service account, or scoped token).
- Inbox and outbox paths, including ownership and permissions.
- Expected delivery convention: polling, webhook, or scheduled transfer.
- DOCX naming convention and maximum file size.
- JSON schema/version, encoding, and relationship between JSON and DOCX files.
- Completion/acknowledgement convention and retry behavior.
- Whether the test server can reach the dashboard, or the dashboard must pull files.

## Safety requirements

- Use a dedicated test account with least-privilege access.
- Keep credentials outside Git and rotate them if exposed.
- Use an allowlisted host and verify SSH host keys / TLS certificates.
- Write uploads atomically; do not process partial files.
- Validate JSON against a versioned schema and treat all transferred content as untrusted.
- Make processing idempotent and preserve an audit trail.
- Never point this integration at production without a separately reviewed change.

## Planned flow

1. Discover a completed delivery in the test-server inbox.
2. Verify metadata and file integrity.
3. Register the document and its JSON metadata.
4. Make it available in the reviewer dashboard.
5. Record reviewer comments and decisions.
6. Publish the approved/rejected result to the configured test-server outbox.
7. Record transfer acknowledgement and any retry/error state.
