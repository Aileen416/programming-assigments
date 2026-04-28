"""Module for reversing case of strings in a list."""


def reverse_lower_and_upper_case(items: list[str]) -> list[str]:
    """Reverse lowercase and uppercase strings in a list."""
    result = []
    for item in items:
        if item.islower():
            result.append(item.upper())
        elif item.isupper():
            result.append(item.lower())
    return result
