# GitHub Repository Traffic Analyzer

This project provides a Python script to fetch and display traffic data (views and clones) for all repositories of a specified GitHub user. It utilizes the GitHub API to gather information on how many people viewed and cloned each repository.

## Features

- Fetch a list of all repositories for a specified GitHub user.
- Retrieve traffic views and clones for each repository.
- Display the traffic data for easy analysis.

## Prerequisites

- Python 3.x
- A GitHub personal access token with appropriate permissions to access repository data.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install required Python packages:**

    This script requires the `requests` library. You can install it using pip:

    ```bash
    pip install requests
    ```

## Setup

1. **Generate a GitHub Personal Access Token:**

    - Go to your GitHub account.
    - Navigate to `Settings` > `Developer settings` > `Personal access tokens`.
    - Generate a new token with the `repo` scope.

2. **Update the script with your credentials:**

    Replace the placeholders in the script with your actual GitHub token and username:

    ```python
    GITHUB_TOKEN = "YOUR-API-KEY"
    USERNAME = "YOUR-USER-NAME"
    ```

## Usage

1. **Run the script:**

    Execute the Python script to fetch and display the traffic data:

    ```bash
    python script_name.py
    ```

2. **Output:**

    The script will output the repository names, along with their traffic views and clones, in the terminal:

    ```
    Repository: repo-name
    Views: {'count': X, 'uniques': Y}
    Clones: {'count': X, 'uniques': Y}
    -------------
    ```

## Troubleshooting

- If you encounter issues with API access, ensure your GitHub token has the correct permissions.
- API rate limits may apply. If the script fails due to rate limits, wait and try again later.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- This project uses the [GitHub API](https://docs.github.com/en/rest) to fetch repository data.
- Special thanks to the open-source community for making such resources available.
