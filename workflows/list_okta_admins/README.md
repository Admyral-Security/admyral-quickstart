# Okta List Admins

This workflow retrieves all admin users.

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

- [Okta](https://docs.admyral.dev/integrations/okta/okta)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **Okta**: `okta_secret`
> If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
> e.g `secrets = {"OKTA_SECRET": "your_secret_name"}` \

## Set Up Workflow

1. Open the `list_okta_admins.py` file
2. Adjust the search query for user type of interest

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push list_okta_admins -f workflows/list_okta_admins/list_okta_admins.py --activate
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
poetry run admyral workflow trigger list_okta_admins
```
