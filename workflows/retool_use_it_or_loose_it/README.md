# Retool User Inactivity Check Workflow

This workflow checks for inactive Retool users who have not logged in for a specified period (default: 60 days) and sends a Slack message to that user, asking if they still need access to Retool.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [Retool](https://docs.admyral.dev/integrations/retool/retool)
- [Slack](https://docs.admyral.dev/integrations/slack/slack)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
>
> **Retool**: `retool_secret` \
> **Slack**: `slack_secret` \
>  If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
>  e.g `secrets = {"RETOOL_SECRET": "your_secret_name"}` and for Slack respectively. \

## Set Up Workflow

There are no adjustments required for the workflow to work, however you can optionally:

Adjust the threshold, determining if a user should be counted as inactive by changing the value of `inactivity_threshold` within the workflow function.

Use the CLI to push the custom actions:

```bash
poetry run admyral action push build_retool_inactivity_question_as_slack_messages -a workflows/retool_use_it_or_loose_it/retool_use_it_or_loose_it.py
```

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push retool_use_it_or_loose_it -f workflows/retool_use_it_or_loose_it/retool_use_it_or_loose_it.py --activate
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
poetry run admyral workflow trigger retool_use_it_or_loose_it
```
