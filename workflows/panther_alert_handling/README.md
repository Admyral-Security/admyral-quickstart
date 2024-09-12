# Panther Alert Handling

This workflow handles alerts from Panther, specifically focusing on AWS ALB alerts for a high volume of 4xx errors. It uses AI to generate summaries and recommendations, creates a Jira issue for tracking, and notifies the team via Slack.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [Slack](https://docs.admyral.dev/integrations/slack/slack)
- [Jira](https://docs.admyral.dev/integrations/jira/jira)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **Slack**: `slack_secret` \
> **Jira**: `jira_secret` \
> If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
> e.g `secrets = {"SLACK_SECRET": "your_secret_name"}` and for Jira respectively.

## Set Up Workflow

1. Open the `panther_alert_handling.py` file
2. Set the Slack channel ID in `channel_id` where the notifications should be sent

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push panther_alert_handling -f workflows/panther_alert_handling/panther_alert_handling.py --activate
```

## Expected Payload

The workflow expects the following payload schema:

```json
{
  "alert": {
    "id": "AWS.ALB.HighVol400s",
    "title": "your_alert_title",
    "event_details": {
      "domain_name": "your_domain"
    },
    "account": "your_account",
    "mitre_attack": {
      "tactic": "your_mitre_attack_tactic",
      "technique": "your_mitre_attack_technique"
    },
    "severity": "your_alert_priority"
  }
}
```

## Run Workflow

Use the Admyral UI:

1. Open the workflow in the workflow No-Code editor
2. Click on **Run**
3. Click on **Run Workflow**

Or use the CLI to trigger the workflow:

```bash
poetry run admyral workflow trigger panther_alert_handling -p '{"alert": {"id": "AWS.ALB.HighVol400s", "title": "your_alert_title", "event_details": {"domain_name": "your_domain"}, "account": "your_account", "mitre_attack": {"tactic": "your_mitre_attack_tactic", "technique": "your_mitre_attack_technique"}, "severity": "your_alert_priority"}}'

```
