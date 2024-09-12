# Analyze URL Workflow

The workflow uses VirusTotal to analyze a URL.

## Required Secrets

To use this workflow, the following secret is required. To set it up, please follow the respective guide on the linked documentation page.

- [VirusTotal](https://docs.admyral.dev/integrations/virus_total/virus_total)

> [!IMPORTANT]
> The workflow expects the following secret name: \
> VirusTotal: virus_total

## Set Up Workflow

Use the `admyral` CLI to push the workflow:

```bash
poetry run admyral workflow push analyze_url -f workflows/analyze_url/analyze_url.py --activate
```

## Expected Payload

The workflow expects the following payload:

```json
{
  "url": "your_url_to_analyze"
}
```

## Run Workflow

Use the Admyral UI:

1. Open the workflow, by clicking on the **>** icon in the Workflow Overview
2. Click on **Run**
3. Input the expected payload
4. Click on **Run Workflow**

Use the `admyral` CLI to trigger the workflow:

```bash
poetry run admyral workflow trigger analyze_url -p '{"url": "your_url_to_analyze"}'
```
