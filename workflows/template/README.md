# Monitor GitHub Org Owner Changes

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

-

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
>
> If your secrets have a different name, please adjust the secret mappings in the workflow function accordingly \
> e.g `secrets = {"<>": "your_secret_name"}` \

## Set Up Workflow

1.

Use the CLI to push the custom actions:

```bash
poetry run admyral action push
```

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push  --activate
```

## Expected Payload

The workflow expects the following payload schema:

```json
{
  "": ""
}
```

> [!IMPORTANT]
> The workflow doesn't expect any payload.

## Run Workflow

Use the Admyral UI:

1. Open the workflow in the workflow No-Code editor
2. Click on **Run**
3. Click on **Run Workflow**

Use the CLI to trigger the workflow:

```bash
poetry run admyral workflow trigger
```
