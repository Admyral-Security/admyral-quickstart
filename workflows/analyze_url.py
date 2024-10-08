from admyral.workflow import workflow, Webhook
from admyral.typings import JsonValue
from admyral.actions import (
    virus_total_analyze_url
)


@workflow(
    description="Analyze file hash",
    triggers=[Webhook()]
)
def analyze_url(payload: dict[str, JsonValue]):
    virus_total_analyze_url(
        url=payload["url"],
        secrets={"VIRUS_TOTAL_SECRET": "virustotal_api_key"}
    )


if __name__ == "__main__":
    # Execute your workflow as a normal Python script
    result = analyze_url({"url": "https://www.google.com"})
    print(result)
