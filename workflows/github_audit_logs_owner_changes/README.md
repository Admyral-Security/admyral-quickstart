# GitHub Audit Logs Owner Changes Workflow

This workflow analyzes the GitHub Audit logs for a specified enterprise for the last hour to check if there were any owner changes within that enterprise. In case there were changes, a notification via Slack is being sent.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [GitHub Enterprise](https://docs.admyral.dev/integrations/github/github)
- [Slack](https://docs.admyral.dev/integrations/slack/slack)

> [!IMPORTANT]
> The workflow expects the following secret names: \
> Slack: slack_secret
> GitHub Enterprise: github_enterprise_secret

## Set Up Workflow

1. Open the `github_audit_logs_owner_changes.py` file.
2. Adjust the `enterprise` and `email` with your enterprise slug and the email of the person to be notified of the respective events via slack

Use the `admyral` CLI to push the custom actions:

```bash
poetry run admyral action push get_time_range_of_last_full_hour -a workflows/github_audit_logs_owner_changes/github_audit_logs_owner_changes.py
```

```bash
poetry run admyral action push build_info_message_owner_changes -a workflows/github_audit_logs_owner_changes/github_audit_logs_owner_changes.py
```

Use the `admyral` CLI to push the workflow:

```bash
poetry run admyral workflow push github_audit_logs_owner_changes -f workflows/github_audit_logs_owner_changes/github_audit_logs_owner_changes.py --activate
```

## Expected Payload

> [!IMPORTANT]
> The workflow doesn't expect any payload.

## Run Workflow

Use the Admyral UI:

1. Open the workflow, by clicking on the **>** icon in the Workflow Overview
2. Click on **Run**
3. Click on **Run Workflow**

You can run the workflow from the Admyral UI or using the `admyral` CLI:

```bash
poetry run admyral workflow trigger github_audit_logs_owner_changes
```
