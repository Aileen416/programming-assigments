"""Solution for task 3."""


def age_counter(text):
    """Count how many people have each age and print ages from 20 to 30."""
    text = text.replace(" ", "")
    people = text.split(",")
    ages = {}
    counter = 0

    for person in people:
        age = int(person.split("=")[1])

        if age in ages:
            ages[age] += 1
        else:
            ages[age] = 1

        if 20 <= age <= 30:
            counter += 1

    print(counter)
    return ages
