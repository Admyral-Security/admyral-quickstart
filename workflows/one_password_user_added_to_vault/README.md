# 1Password User Added to Vault

This workflow monitors 1Password vault events, filtering audit logs to find users who were added to specific vaults. It then sends a Slack notification to the user managing the vault, summarizing the relevant activity. It is scheduled to run at every full hour, checking the previous hour.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [1Password](https://docs.admyral.dev/integrations/1password/1password)
- [Slack](https://docs.admyral.dev/integrations/slack/slack)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **1Password**: `1password_secret` \
> **Slack**: `slack_secret`\
> If your secrets have a different name, please adjust the secret \
> mappings in the workflow function accordingly \
> e.g `secrets = {"SLACK_SECRET": "your_secret_name"}` and for 1password respectively. \

## Set Up Workflow

1. Open the `one_password_user_added_to_vault.py` file
2. Adjust the `user_email` with the email of the person who should be notified
3. Adjust the `vault_id` with your Vault ID for which the audit events should be filtered

Use the CLI to push the custom actions:

```bash
poetry run admyral action push get_time_range_of_last_full_hour -a workflows/one_password_user_added_to_vault/one_password_user_added_to_vault.py
```

```bash
poetry run admyral action push filter_by_vault_and_build_slack_message -a workflows/one_password_user_added_to_vault/one_password_user_added_to_vault.py
```

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push one_password_user_added_to_vault -f workflows/one_password_user_added_to_vault/one_password_user_added_to_vault.py --activate
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
poetry run admyral workflow trigger one_password_user_added_to_vault
```
