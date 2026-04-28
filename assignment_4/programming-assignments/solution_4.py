"""Solution for task 4."""


def numbers_and_bools(lst):
    """Return booleans and numbers from the list."""
    bools = []
    nums = []

    for item in lst:
        if isinstance(item, bool):
            bools.append(item)
        elif isinstance(item, (float, int)):
            nums.append(item)

    return bools, nums
