# Jira Notify User Creation

This workflow monitors Jira for newly created user accounts and sends a Slack notification with relevant details.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [Jira](https://docs.admyral.dev/integrations/jira/jira)
- [Slack](https://docs.admyral.dev/integrations/slack/slack)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **Slack**: `slack_secret` \
> **Jira**: `jira_secret` \
> If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
> e.g `secrets = {"JIRA_SECRET": "your_secret_name"}` \
> and for **Slack** respectively

## Set Up Workflow

1. Open the `jira_notification_user_created.py` file
2. Adjust the `email` with the email of the person to receive the slack notification

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push jira_notification_user_created workflows/jira_notification_user_created/jira_notification_user_created.py --activate
```

## Expected Payload

The workflow expects the following payload schema:

> [!IMPORTANT]
> The workflow doesn't expect any payload.

## Run Workflow

Use the Admyral UI:

1. Open the workflow in the workflow No-Code editor
2. Click on **Run**
3. Click on **Run Workflow**

Or use the CLI to trigger the workflow:

```bash
poetry run admyral workflow trigger jira_notification_user_created
```
