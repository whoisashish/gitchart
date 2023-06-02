import datetime
from github import Github

# GitHub credentials
username = "your-username"
access_token = "your-access-token"

# Create a GitHub instance
g = Github(access_token)

# Get the authenticated user
user = g.get_user(username)

# Get the current year
current_year = datetime.datetime.now().year

# Loop through each day of the year
for month in range(1, 13):
    for day in range(1, 32):
        try:
            # Create a new commit on that day
            date = datetime.datetime(current_year, month, day)
            user.create_repo("Ashish", description="GitHub contribution", auto_init=True)
            repo = user.get_repo("Ashish")
            repo.create_file("README.md", "Initial commit", "Ashish", branch="master")
        except Exception as e:
            print(f"Error: {e}")
