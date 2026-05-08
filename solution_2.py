"""Functions for flattening sequences."""

from itertools import chain


def flatten_sequences(list1, list2):
    """Return a new list with elements from list1 followed by list2."""
    return list(chain(list1, list2))
