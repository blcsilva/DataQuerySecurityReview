# BigQuery Security Setup

This project aims to enhance the security of Google Cloud BigQuery by implementing a set of security controls, including IP-based restrictions, IAM roles, and permissions management. The following instructions detail how to set up and configure these security rules effectively.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Security Rules Implemented](#security-rules-implemented)
- [Running the Security Setup Script](#running-the-security-setup-script)
- [License](#license)

## Project Overview

BigQuery is a powerful analytics data warehouse that requires stringent security measures to protect sensitive data. This project implements security controls to ensure that access is restricted to authorized users and IP addresses only.

## Prerequisites

Before running this project, ensure you have the following:

- A Google Cloud account with access to BigQuery.
- The Google Cloud SDK installed and configured.
- Python 3.6 or later.
- Required Python packages:
  ```bash
  pip install google-cloud-bigquery google-cloud-compute google-auth
  ```

## Setup Instructions

1. **Set Up Google Cloud Credentials**:
   - Create a service account with the necessary permissions for BigQuery and Compute Engine.
   - Download the service account JSON key file.

2. **Store Credentials Securely**:
   - For local development, you can set an environment variable to point to your JSON key file:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
     ```
   - In CI/CD environments like GitHub Actions, add your JSON credentials as a secret.

3. **Configure IAM Roles**:
   - Define roles and permissions necessary for the users and service accounts accessing BigQuery.

4. **Implement IP-Based Restrictions**:
   - Create a list of trusted IP addresses and configure firewall rules to allow access only from those addresses.

## Security Rules Implemented

This project implements the following security rules for BigQuery:

- **IP-Based Access Control**:
  - Only specified IP addresses can access BigQuery resources.

- **IAM Role Assignments**:
  - Roles such as `roles/bigquery.dataViewer`, `roles/bigquery.jobUser`, and custom roles are assigned to ensure principle of least privilege.

- **Logging and Monitoring**:
  - Enable logging for all BigQuery operations to monitor access and identify potential unauthorized access attempts.

## Running the Security Setup Script

To apply the security configurations, run the provided Python script:

```bash
python security_setup.py
```

Ensure that your environment is configured with the necessary credentials before running the script.

## License

This project is licensed under the MIT License.


