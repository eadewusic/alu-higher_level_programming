#!/usr/bin/python3
# 100-github_commits.py
"""This module or script
fetches the last 10 commits of the
specified repository by the given owner
using the GitHub API.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository> <owner>".format(sys.argv[0]))
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'

    try:
        response = requests.get(url)
        commits = response.json()

        if isinstance(commits, list):
            for commit in commits[:10]:
                sha = commit.get('sha')
                author_name = commit.get('commit', {}).get('author', {}).get('name')
                print(f"{sha}: {author_name}")
    except Exception as e:
        print(e)
