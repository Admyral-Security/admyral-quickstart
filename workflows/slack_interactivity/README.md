# Handle Slack Interactivity Responses

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [Slack](https://docs.admyral.dev/integrations/slack/slack)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **Slack**: `slack_secret`
> If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
> e.g `secrets = {"SLACK_SECRET": "your_secret_name"}` \

## Set Up Workflow

1. Open the `slack_interactivity.py` file
2. Adjust the `channel_id` with your Channel ID

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push slack_interactivity -f workflows/slack_interactivity/slack_interactivity.py --activate
```

## Expected Payload

The workflow expects the following payload schema:

```json
{
  "actions": [
    {
      "action_id": "your_action_id", // one of: {use_it_or_loose_it, access_review}
      "value": {
        "user": "your_user",
        "group": "your, group",
        "reason": "your_reason"
      }
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
poetry run admyral workflow trigger -p '"actions": [
{
  "action_id": "your_action_id", // one of: {use_it_or_loose_it, access_review}
    "value": {
      "user": "your_user",
      "group": "your, group",
      "reason": "your_reason"
    }
  }]
}'
```
