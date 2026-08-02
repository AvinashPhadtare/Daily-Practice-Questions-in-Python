def deduplicate_checkins(checkins):
    seen = set()          # Stores IDs we've already seen
    result = []           # Stores unique check-ins in original order

    for member_id in checkins:   # Go through every check-in
        if member_id not in seen:  # If this ID is new
            seen.add(member_id)    # Remember it
            result.append(member_id)  # Keep it in the result

    return result


def members_present_in_both(day1, day2):
    return set(day1) & set(day2)


# Example Usage
checkins = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(deduplicate_checkins(checkins))
# Output: [3, 1, 4, 5, 9, 2, 6]

day1 = [1, 2, 3, 4]
day2 = [3, 4, 5, 6]
print(members_present_in_both(day1, day2))
# Output: {3, 4}
