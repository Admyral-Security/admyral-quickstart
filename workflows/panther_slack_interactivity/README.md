# Panther Handle Slack Interactivity

This workflow manages Slack interactivity responses, specifically handling actions related to Panther alerts by updating Jira issues.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [Jira](https://docs.admyral.dev/integrations/jira/jira)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **Jira**: `jira_secret` \
> If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
> e.g `secrets = {"JIRA_SECRET": "your_secret_name"}`.

## Set Up Workflow

There are no adjustments required for the workflow to work

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push panther_slack_interactivity -f workflows/panther_slack_interactivity/panther_slack_interactivity.py --activate

```

## Expected Payload

The workflow expects the following payload schema:

```json
{
  "actions": [
    {
      "action_id": "your_action_id", // one of {panther_alert_handling-suspicious, panther_alert_handling-non-suspicious}
      "value": "your_jira_issue_id_or_key"
    }
  ]
}
```

## Run Workflow

Use the Admyral UI:

1. Open the workflow in the workflow No-Code editor
2. Click on **Run**
3. Click on **Run Workflow**

Or use the CLI to trigger the workflow:

```bash
poetry run admyral workflow trigger panther_slack_interactivity -p '{"actions": [{"action_id": "your_action_id", "value": "your_jira_issue_id_or_key"}]}'
```
