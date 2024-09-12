# Okta User Inactivity Check Workflow

This workflow checks for inactive Okta users who have not logged in for a specified period (default: 90 days) and sends a Slack message to that user, asking if they still need access to Okta.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [Okta](https://docs.admyral.dev/integrations/okta/okta)
- [Slack](https://docs.admyral.dev/integrations/slack/slack)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **Okta**: `okta_secret` \
> **Slack**: `slack_secret` \
> If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly. \
> e.g. `secrets = {"OKTA_SECRET": "your_secret_name"}` and similarly for Slack.

## Set Up Workflow

There are no adjustments required for the workflow to work, however you can optionally:

1. Add a search filter to the `search` parameter
2. Adjust, how many users should be checked for inactivity with the `limit` parameter
3. Adjust the threshold, determining if a user should be counted as inactive by changing the value of `inactivity_threshold`

Use the CLI to push the custom actions:

```bash
poetry run admyral action push filter_inactive_okta_users -a workflows/okta_use_it_or_lose_it/okta_use_it_or_lose_it.py
```

```bash
poetry run admyral action push build_okta_inactivity_messages -a workflows/okta_use_it_or_lose_it/okta_use_it_or_lose_it.py
```

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push okta_use_it_or_lose_it -f workflows/okta_use_it_or_lose_it/okta_use_it_or_lose_it.py --activate
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
poetry run admyral workflow trigger okta_use_it_or_lose_it
```
