"""Functions for geometric mean and median."""

from statistics import geometric_mean, median


def gm_median(values):
    """Return (geometric_mean, median) of valid numeric values or None."""
    if not values:
        return None

    filtered = [
        v for v in values
        if isinstance(v, (int, float)) and v > 0
    ]

    if not filtered:
        return None

    return (geometric_mean(filtered), median(filtered))
