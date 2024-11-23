# GitHub Activity CLI

A simple command-line interface tool that fetches and displays the latest activities of a GitHub user. The tool shows various GitHub events including stars, commits, pull requests, issues, and more.

This is one of the exercises at roadmap.sh   
[Link to the project](https://roadmap.sh/projects/github-user-activity)

## Features

- Fetch real-time GitHub activity for any public user profile
- Display multiple types of GitHub events:
  - Repository stars (Watch events)
  - Push events
  - Pull request activities (creation, reviews, comments)
  - Issue activities (creation, comments)
  - Repository creation events
  - And more GitHub events

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone this repository or download the script:
```bash
git clone <repository-url>
```

2. Install the required dependencies:
```bash
pip install requests
```

## Usage

Run the script from the command line with a GitHub username as an argument:

```bash
python github-activity.py <github-username>
```

Example:
```bash
python github-activity.py kamranahmedse
```

### Output Format

The tool will display activities in the following format:
- Starred repositories: `Starred owner/repository`
- Push events: `Pushed commit to owner/repository`
- Pull requests: `Created pull request #number`
- Pull request reviews: `Reviewed pull request #number`
- Pull request comments: `Commented on pull request #number`
- Issues: `Open a new issue in owner/repository`
- Comments: `Commented on owner/repository`
- Creation events: `Created {type} {name}`

## Error Handling

The tool includes error handling for:
- Invalid or missing GitHub usernames
- Network request failures
- API response errors
- Request timeouts (10-second timeout)

## Limitations

- Only works with public GitHub profiles
- Subject to GitHub API rate limiting
- Displays only recent activities (as returned by the GitHub Events API)

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).