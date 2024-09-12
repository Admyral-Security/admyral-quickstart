# Analyze URL Workflow

The workflow uses VirusTotal to analyze a URL.

## Required Secrets

To use this workflow, the following secret is required. To set it up, please follow the respective guide on the linked documentation page.

- [VirusTotal](https://docs.admyral.dev/integrations/virus_total/virus_total)

> [!IMPORTANT]
> The workflow currently expects the following secret names: \
> **VirusTotal**: `virus_total` \
> If your secret has a different name, please adjust the secret mapping in the workflow function accordingly \
> e.g `secrets = {"VIRUS_TOTAL_SECRET": "your_secret_name"}`

## Set Up Workflow

Use the CLI to push the workflow:

```bash
poetry run admyral workflow push analyze_url -f workflows/analyze_url/analyze_url.py --activate
```

## Expected Payload

The workflow expects the following payload schema:

```json
{
  "url": "your_url_to_analyze"
}
```

## Run Workflow

Use the Admyral UI:

1. Open the workflow in the workflow No-Code editor
2. Click on **Run**
3. Input the payload following the expeted schema
4. Click on **Run Workflow**

Use the CLI to trigger the workflow:

```bash
poetry run admyral workflow trigger analyze_url -p '{"url": "your_url_to_analyze"}'
```
