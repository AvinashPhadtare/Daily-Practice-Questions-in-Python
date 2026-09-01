# ========================= Question ========================
# Q46. Using requests.Session() with GitHub API
#
# GitHub's public API:
# https://api.github.com
#
# Use requests.Session() to:
#
# - Set a User-Agent header once for all requests.
# - Fetch the user's public profile.
# - Fetch the user's public repositories.
# - Fetch languages for every repository.
#
# Create:
#
#     github_profile_summary(username: str) -> dict
#
# Return:
#
# {
#     "name": str,
#     "followers": int,
#     "public_repos": int,
#     "most_used_languages": list
# }
#
# Sort most_used_languages by frequency across all repos.
#
# ============================================================


import requests


# ------------------------------------------------------------
# Function to create a GitHub profile summary
# ------------------------------------------------------------
def github_profile_summary(username: str) -> dict:

    # GitHub API base URL.
    base_url = "https://api.github.com"

    # Create one Session object.
    #
    # We will reuse this same session for all API requests.
    session = requests.Session()

    # Set the User-Agent once.
    #
    # Every request made using this session will use this header.
    session.headers.update({
        "User-Agent": "GitHub-Profile-Summary"
    })

    # --------------------------------------------------------
    # 1. Fetch the user's public profile
    # --------------------------------------------------------

    # Build the profile API URL.
    profile_url = f"{base_url}/users/{username}"

    # Send GET request using the same session.
    response = session.get(profile_url)

    # Raise an exception if the request failed.
    response.raise_for_status()

    # Convert JSON response into a Python dictionary.
    profile = response.json()

    # --------------------------------------------------------
    # 2. Fetch the user's public repositories
    # --------------------------------------------------------

    # Build repositories API URL.
    repos_url = f"{base_url}/users/{username}/repos"

    # Request repositories.
    response = session.get(repos_url)

    # Check for HTTP errors.
    response.raise_for_status()

    # Convert JSON response into a Python list.
    repos = response.json()

    # --------------------------------------------------------
    # 3. Store total language usage
    # --------------------------------------------------------

    # Dictionary to store total language counts
    # across all repositories.
    language_totals = {}

    # Loop through every repository.
    for repo in repos:

        # Get repository name.
        repo_name = repo["name"]

        # Build the languages API URL.
        languages_url = (
            f"{base_url}/repos/{username}/{repo_name}/languages"
        )

        # Fetch languages for this repository.
        response = session.get(languages_url)

        # Check for HTTP errors.
        response.raise_for_status()

        # Convert JSON response into a dictionary.
        languages = response.json()

        # ----------------------------------------------------
        # Add this repository's language counts to totals.
        # ----------------------------------------------------

        for language, count in languages.items():

            # Add the current count to the existing total.
            #
            # If the language doesn't exist yet,
            # .get(language, 0) gives us 0.
            language_totals[language] = (
                language_totals.get(language, 0) + count
            )

    # --------------------------------------------------------
    # 4. Sort languages by usage
    # --------------------------------------------------------

    # Sort language names according to their total count.
    #
    # reverse=True means highest count comes first.
    most_used_languages = sorted(
        language_totals,
        key=language_totals.get,
        reverse=True
    )

    # --------------------------------------------------------
    # 5. Create final result
    # --------------------------------------------------------

    result = {
        "name": profile["name"],
        "followers": profile["followers"],
        "public_repos": profile["public_repos"],
        "most_used_languages": most_used_languages
    }

    # Return the final dictionary.
    return result


# ============================================================
# Example Usage
# ============================================================

# Replace this with any GitHub username whose public profile
# you want to inspect.
username = "octocat"

# Call the function.
summary = github_profile_summary(username)

# Display the result.
print("GitHub Profile Summary")
print("----------------------")

print("Name:", summary["name"])
print("Followers:", summary["followers"])
print("Public Repositories:", summary["public_repos"])

print("Most Used Languages:")
for language in summary["most_used_languages"]:
    print("-", language)
