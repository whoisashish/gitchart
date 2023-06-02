import datetime
from github import Github

# Configure your GitHub Enterprise instance details
github_instance_url = "https://sgithub.fr.world.socgen"
github_username = "ashish-yadav"
github_password = "your_password"  # Replace with your password or use an access token

# Configure the start and end date of the contribution period
start_date = datetime.datetime(2023, 1, 1)
end_date = datetime.datetime(2023, 12, 31)

# Configure the ASCII art for the contribution
ascii_art = [
    "0000011000110000",
    "0001111101111100",
    "0001111101111100",
    "0001111101111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
    "0001111111111100",
]

# Connect to the GitHub Enterprise instance
g = Github(base_url=github_instance_url, login_or_token=github_username, password=github_password)

# Get the authenticated user
user = g.get_user()

# Loop through the dates within the specified period
current_date = start_date
while current_date <= end_date:
    # Get the current contribution count for the date
    contributions = user.get_contributions(year=current_date.year, month=current_date.month, day=current_date.day)

    # Set the contribution count according to the ASCII art pattern
    for i in range(len(ascii_art)):
        for j in range(len(ascii_art[i])):
            if ascii_art[i][j] == "1":
                contributions[i * 7 + j].count = 1

    # Commit the updated contributions
    user.create_contributions(contributions)

    # Move to the next date
    current_date += datetime.timedelta(days=1)

print("Contributions created successfully!")
