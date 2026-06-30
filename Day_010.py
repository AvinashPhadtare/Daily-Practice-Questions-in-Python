import requests


class APIError(Exception):
    pass


def get_users_by_city(city: str) -> list:
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Call API
        response = requests.get(url, timeout=5)

        # Check status code
        if response.status_code != 200:
            raise APIError(
                f"API request failed with status code {response.status_code}"
            )

        users = response.json()

        result = []

        # Filter users by city (case-insensitive)
        for user in users:
            user_city = user["address"]["city"]

            if user_city.lower() == city.lower():
                result.append(
                    {
                        "id": user["id"],
                        "name": user["name"],
                        "email": user["email"],
                    }
                )

        return result

    except requests.exceptions.RequestException as e:
        raise APIError(f"API request failed: {e}")

    except Exception as e:
        raise APIError(f"Unexpected error: {e}")


# Example usage
try:
    users = get_users_by_city("Gwenborough")

    print("Users found:")
    for user in users:
        print(user)

except APIError as e:
    print(f"Error: {e}")