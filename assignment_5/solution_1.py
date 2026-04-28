"""Functions for grouping words by first letter."""

from collections import defaultdict


def group_by_first_letter(words):
    """Return a dictionary grouping words by their first letter."""
    grouped = defaultdict(list)

    for word in words:
        if word:
            grouped[word[0]].append(word)

    return dict(grouped)
