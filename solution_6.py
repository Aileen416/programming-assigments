"""Functions for validating datetime strings."""

from datetime import datetime


def datetime_validator(date_str):
    """Return a datetime object if valid format, otherwise None."""
    date_str = date_str.strip()

    formats = [
        "%B %d, %Y, %H:%M:%S",  # full month name
        "%b %d, %Y, %H:%M:%S",  # abbreviated month name
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    return None
