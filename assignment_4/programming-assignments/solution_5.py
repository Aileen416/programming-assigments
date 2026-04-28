"""Solution for task 5."""


def lists_intersection(a, b):
    """Return common elements."""
    if not isinstance(a, list) or not isinstance(b, list):
        return None

    result = []

    for item in a:
        if item in b and item not in result:
            result.append(item)

    return result
