"""Solution for task 6."""


def person_number_validate(pnr):
    """Validate Swedish personal number."""
    if not isinstance(pnr, str) or len(pnr) != 10 or not pnr.isdigit():
        return False

    month = int(pnr[2:4])
    day = int(pnr[4:6])

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:
        return False

    if day < 1 or day > days_in_month[month - 1]:
        return False

    total = 0

    for index in range(9):
        number = int(pnr[index])

        if index % 2 == 0:
            number *= 2

        if number > 9:
            number -= 9

        total += number

    check_digit = (10 - total % 10) % 10

    return check_digit == int(pnr[9])
