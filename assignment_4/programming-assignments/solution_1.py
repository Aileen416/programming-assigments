"""Solution for assignment points calculation."""


def assignment_points(assignments_list: list[str]) -> int:
    """Return points based on number of 'Approved' assignments."""
    if len(assignments_list) != 7:
        return 0
    count = assignments_list.count("Approved")
    points = [0, 1, 2, 4, 6, 9, 12, 15]
    return points[count]
