"""Functions for finding most common words."""

from collections import Counter


def most_common_words(words, n):
    """Return the n most common words as (word, count) tuples."""
    if n < 1 or not words:
        return None

    counts = Counter(words)

    return counts.most_common(n)
