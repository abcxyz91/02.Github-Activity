import requests
import sys
import json

BASE_URL = "https://api.github.com/users/"

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python script.py <github-username>")
    else:
        username = sys.argv[1]
        activity(username)


def activity(username):
    request_url = f"{BASE_URL}{username}/events"
    try:
        response = requests.get(request_url, timeout=10)
        if response.status_code == 200:
            events = response.json()

            if not events:
                print(f"No recent activity found for user {username}")
                return

            print("Output:")
            for event in events:
                if event["type"] == "WatchEvent":
                    print(f"- Starred {event['repo']['name']}")
                elif event["type"] == "PushEvent":
                    print(f"- Pushed commit to {event['repo']['name']}")
                elif event["type"] == "PullRequestEvent":
                    print(f"- Created pull request {event['payload']['pull_request']['number']}")
                elif event["type"] == "PullRequestReviewEvent":
                    print(f"- Reviewed pull request {event['payload']['pull_request']['number']}")
                elif event["type"] == "PullRequestReviewCommentEvent":
                    print(f"- Commented on pull request {event['payload']['pull_request']['number']}")
                elif event["type"] == "IssuesEvent":
                    print(f"- Open a new issue in {event['repo']['name']}")
                elif event["type"] == "IssueCommentEvent":
                    print(f"- Commented on {event['repo']['name']}")
                elif event["type"] == "CreateEvent":
                    print(f"- Created {event['payload']['ref_type']} {event['payload']['ref']}")
                else:
                    print(f"{event['type']}")

        else:
            print(f"Request error: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    main()