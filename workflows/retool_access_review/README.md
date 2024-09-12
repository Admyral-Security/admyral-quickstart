# Retool Access Review

This workflow automates the process of reviewing Retool access permissions by sending Slack messages to managers for their teams' access review. Managers can review each user's group membership and select whether to approve or remove access for different scenarios.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [Retool](https://docs.admyral.dev/integrations/retool/retool)
- [Slack](https://docs.admyral.dev/integrations/slack/slack)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
>
> - **Retool**: `retool_secret` \
> - **Slack**: `slack_secret`
>   If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
>   e.g `secrets = {"RETOOL_SECRET": "your_secret_name"}` and for Slack respectively. \

## Set Up Workflow

1. Open the `retool_access_review.py` file
2. Adjust the `manager` parameter in the `build_review_requests_as_slack_message_for_managers` function with the email of the person who should be notified via Slack.

Use the CLI to push the custom actions:

```bash
poetry run admyral action push build_review_requests_as_slack_message_for_managers -a workflows/retool_access_review/retool_access_review.py
```

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push retool_access_review -f workflows/retool_access_review/retool_access_review.py --activate
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
poetry run admyral workflow trigger retool_access_review
```
