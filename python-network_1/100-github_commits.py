#!/usr/bin/python3
# 100-github_commits.py
"""
This script fetches the last 10 commits of the specified repository by the given owner
using the GitHub API.

Usage: python3 100-github_commits.py <repository> <owner>
Example: python3 100-github_commits.py rails rails
"""

import sys
import requests

def fetch_github_commits(repository, owner):
    """
    Fetches the last 10 commits of the specified repository by the given owner.

    Args:
        repository (str): The name of the GitHub repository.
        owner (str): The name of the GitHub repository owner.

    Returns:
        list: A list of dictionaries containing the last 10 commits' data.
    """
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository> <owner>".format(sys.argv[0]))
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    try:
        commits = fetch_github_commits(repository, owner)
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name')
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
