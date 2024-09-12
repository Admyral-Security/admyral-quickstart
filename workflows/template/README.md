#

## Required Secrets

To use this workflow, the following secrets are required. To set them up, please follow the respective guide on the linked documentation page.

-

> [!IMPORTANT]
> The workflow expects the following secret name: \

## Set Up Workflow

Use the `admyral` CLI to push the workflow:

```bash
poetry run admyral workflow push <> -f workflows/ --activate
```

## Expected Payload

The workflow expects the following payload:

```json
{}
```

## Trigger Workflow

You can run the workflow from the Admyral UI or using the `admyral` CLI:

```bash
poetry run admyral workflow trigger <> -p '{"": ""}'
```
