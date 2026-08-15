# ========================= Question ========================
# Build a simple JSON-based config file system for a gym app.

# Implement the following functions:
#
# 1. save_config(config: dict, filepath: str)
#    - Save the configuration dictionary to a JSON file.
#    - The JSON file should be pretty-printed.
#
# 2. load_config(filepath: str) -> dict
#    - Load the configuration from the JSON file.
#    - Return the configuration as a dictionary.
#    - If the file does not exist, return an empty dictionary.
#
# 3. update_config(filepath: str, key: str, value)
#    - Load the existing configuration.
#    - Update the given key with the new value.
#    - Save the updated configuration back to the JSON file.
#
# 4. delete_config_key(filepath: str, key: str)
#    - Load the configuration.
#    - Remove the given key if it exists.
#    - Save the updated configuration back to the JSON file.
#
# Test the functions using a gym configuration containing:
# - gym_name
# - max_capacity
# - plans
# ============================================================


# Solution:-
import json


def save_config(config, filepath):
    # Open the file in write mode
    with open(filepath, "w") as file:

        # Convert Python dictionary to JSON
        # indent=4 makes the JSON file pretty-printed
        json.dump(config, file, indent=4)


def load_config(filepath):
    try:
        # Open the JSON file in read mode
        with open(filepath, "r") as file:

            # Convert JSON file data into Python dictionary
            return json.load(file)

    except FileNotFoundError:
        # If file does not exist, return empty dictionary
        return {}


def update_config(filepath, key, value):
    # Load existing configuration
    config = load_config(filepath)

    # Update or add the given key
    config[key] = value

    # Save the updated configuration
    save_config(config, filepath)


def delete_config_key(filepath, key):
    # Load existing configuration
    config = load_config(filepath)

    # Check if the key exists
    if key in config:

        # Remove the key
        del config[key]

        # Save the updated configuration
        save_config(config, filepath)


# Example Usage

config = {
    "gym_name": "FitZone",
    "max_capacity": 200,
    "plans": ["basic", "premium", "vip"]
}


# Save the configuration
save_config(config, "config.json")

print("Initial configuration:")
print(load_config("config.json"))


# Update max_capacity
update_config("config.json", "max_capacity", 300)

print("\nAfter updating max_capacity:")
print(load_config("config.json"))


# Delete plans
delete_config_key("config.json", "plans")

print("\nAfter deleting plans:")
print(load_config("config.json"))


# Try loading a file that does not exist
print("\nReading missing file:")
print(load_config("missing.json"))
