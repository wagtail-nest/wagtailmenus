"""
Called by GitHub Actions when the nightly build fails.
This reports an error to the #nightly-build-failures Slack channel.
"""
import json
import os
import urllib.request


def report_nightly_build_failure():
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print(
            "Unable to report to #nightly-build-failures slack channel because SLACK_WEBHOOK_URL is not set"
        )
        return

    # https://docs.github.com/en/free-pro-team@latest/actions/reference/environment-variables#default-environment-variables
    repository = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]
    url = f"https://github.com/{repository}/actions/runs/{run_id}"

    print("Reporting to #nightly-build-failures slack channel")
    request = urllib.request.Request(
        webhook_url,
        data=json.dumps({
            "text": f"A Nightly build failed. See {url}",
        }).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        print(f"Slack responded with: {response.status}")


if __name__ == "__main__":
    report_nightly_build_failure()
