"""Functions for generating lottery numbers."""

from random import sample


def lottery_numbers(number, upper, lower):
    """Return a list of unique random integers or None if invalid input."""
    if (
        lower < 0
        or upper < 1
        or number < 1
        or (upper - lower) < (number - 1)
    ):
        return None

    return sample(range(lower, upper + 1), number)
