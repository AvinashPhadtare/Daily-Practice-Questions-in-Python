# ========================= Question ========================
# Q45. API Pagination
#
# The API:
# https://jsonplaceholder.typicode.com/posts
#
# returns 100 posts.
#
# Simulate pagination by fetching 10 posts at a time using
# "_start" and "_limit" query parameters.
#
# Write fetch_all_posts_paginated(page_size: int) -> list
# that:
#
# - Fetches all pages until there are no more results.
# - Prints progress for every page.
# - Returns the complete list of posts.
# - Counts the total number of API calls made.
#
# ============================================================


import requests


# ------------------------------------------------------------
# Function to fetch all posts page by page
# ------------------------------------------------------------
def fetch_all_posts_paginated(page_size: int) -> list:

    # API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # This list will store all posts from every page.
    all_posts = []

    # "_start" tells the API where to start fetching.
    start = 0

    # Used only for displaying the page number.
    page = 1

    # Count how many API requests we make.
    api_calls = 0

    # Keep requesting pages until the API returns no posts.
    while True:

        # Parameters sent to the API.
        params = {
            "_start": start,
            "_limit": page_size
        }

        # Make the API request.
        response = requests.get(url, params=params)

        # Count this API call.
        api_calls += 1

        # Raise an error if the request was unsuccessful.
        response.raise_for_status()

        # Convert JSON response into a Python list.
        posts = response.json()

        # Print progress.
        print(f"Fetching page {page}... got {len(posts)} posts")

        # If no posts were returned, there are no more pages.
        if not posts:
            break

        # Add the posts from this page to the complete list.
        all_posts.extend(posts)

        # Move to the starting position of the next page.
        start += page_size

        # Move to the next page number.
        page += 1

    # Print total number of API calls.
    print(f"\nTotal API calls made: {api_calls}")

    # Return all posts.
    return all_posts


# ============================================================
# Example Usage
# ============================================================

# Fetch 10 posts at a time.
posts = fetch_all_posts_paginated(10)

# Display the total number of posts received.
print(f"Total posts fetched: {len(posts)}")

# Display the first post as an example.
print("\nFirst post:")
print(posts[0])
