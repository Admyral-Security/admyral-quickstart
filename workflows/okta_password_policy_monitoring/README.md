# Monitor Okta Password Policy Changes

This workflow monitors changes to the password policies in Okta and sends notifications via Slack with relevant details. The workflow runs at every full hour and checks for updates made during the previous hour.

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

1. Open the `okta_password_policy_monitoring.py` file
2. Adjust the email address in the `send_slack_message_to_user_by_email` action with the email of the Slack user to receive notifications

Use the CLI to push the custom actions:

```bash
poetry run admyral action push get_time_range_of_last_full_hour -a workflows/okta_password_policy_monitoring/okta_password_policy_monitoring.py
```

```bash
poetry run admyral action push get_okta_password_policy_update_logs -a workflows/okta_password_policy_monitoring/okta_password_policy_monitoring.py
```

```bash
poetry run admyral action push format_okta_policy_update_message -a workflows/okta_password_policy_monitoring/okta_password_policy_monitoring.py
```

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push okta_password_policy_monitoring -f workflows/okta_password_policy_monitoring/okta_password_policy_monitoring.py --activate
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
poetry run admyral workflow trigger okta_password_policy_monitoring

```
