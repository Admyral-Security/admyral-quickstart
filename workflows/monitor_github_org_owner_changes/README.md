# Monitor GitHub Org Owner Changes

This workflow analyzes the GitHub Audit logs for a specified enterprise.
It is scheduled to run at every full hour and analyze the previous hour.
In case there were changes, a notification via Slack is being sent.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [GitHub Enterprise](https://docs.admyral.dev/integrations/github/github)
- [Slack](https://docs.admyral.dev/integrations/slack/slack)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **Slack**: `slack_secret` \
> **GitHub Enterprise**: `github_enterprise_secret` \
> If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
> e.g `secrets = {"GITHUB_ENTERPRISE_SECRET": "your_secret_name"}` \
> and for **Slack** respectively

## Set Up Workflow

1. Open the `monitor_github_org_owner_changes.py` file
2. Adjust the `enterprise` and `email` with your enterprise slug and the email of the person to be notified of the respective events via slack

Use the CLI to push the custom actions:

```bash
poetry run admyral action push get_time_range_of_last_full_hour -a workflows/monitor_github_org_owner_changes/monitor_github_org_owner_changes.py
```

```bash
poetry run admyral action push build_info_message_owner_changes -a workflows/monitor_github_org_owner_changes/monitor_github_org_owner_changes.py
```

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push monitor_github_org_owner_changes -f workflows/monitor_github_org_owner_changes/monitor_github_org_owner_changes.py --activate
```

## Expected Payload

> [!IMPORTANT]
> The workflow doesn't expect any payload.

## Run Workflow

Use the Admyral UI:

1. Open the workflow in the workflow No-Code editor
2. Click on **Run**
3. Click on **Run Workflow**

Or use the CLI to trigger the workflow:

```bash
poetry run admyral workflow trigger monitor_github_org_owner_changes
```
