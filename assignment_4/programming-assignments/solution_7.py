"""Solution for task 7."""


def validating_sum_of_squares(sequence):
    """Return True if element is sum of two squares, else False."""
    result = []

    for item in sequence:
        try:
            number = float(item)
        except (TypeError, ValueError):
            result.append(False)
            continue

        # måste vara ett icke-negativt heltal
        if number < 0 or number != int(number):
            result.append(False)
            continue

        number = int(number)
        valid = False

        # smartare loop (behöver inte gå hela vägen till number)
        for i in range(int(number ** 0.5) + 1):
            remaining = number - i * i
            j = int(remaining ** 0.5)

            if j * j == remaining:
                valid = True
                break

        result.append(valid)

    return result
