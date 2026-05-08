"""Functions for generating random mobile numbers."""

from random import Random


def random_mobile_number_generator(seed=None):
    """Return a randomly generated mobile number as a string."""
    rng = Random(seed)

    prefix = rng.choice(["0", "46", "+46"])
    first_digit = rng.choice(["3", "7"])
    remaining_digits = "".join(str(rng.randint(0, 9)) for _ in range(8))

    return prefix + first_digit + remaining_digits
