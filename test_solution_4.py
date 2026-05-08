# test cell
# testing the probability
import collections
import random
from unittest.mock import patch


def test_solution_4() -> None:
    try:
        import solution_4
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_4 import random_mobile_number_generator
    except:
        raise ValueError("The module does not have the necessary function!")

    n1 = random_mobile_number_generator(seed=123)
    n2 = random_mobile_number_generator(seed=123)
    n3 = random_mobile_number_generator(seed=124)

    assert n1 == n2, "When seed is provided, output must be deterministic (same seed => same output)."
    assert n1 != n3, "Different seeds should (very likely) yield different outputs."

    idx_digit = random.randint(1, 8)
    number_samples = 100000
    count_prefix = collections.defaultdict(int)
    count_digit = collections.defaultdict(int)
    valid_prefixes = ["0", "46", "+46"]

    for i in range(number_samples):
        number = random_mobile_number_generator()
        res = [number.startswith(prefix) for prefix in valid_prefixes]
        assert any(res) == True, f"Generated number {number} is invalid due to incorrect \
    prefix. Check the rules again."
        prefix = valid_prefixes[res.index(True)]
        count_prefix[prefix] += 1
        remaining_part = number.replace(prefix, '', 1)
        assert remaining_part.isdigit() == True, f"Generated number {number} is invalid \
    due to incorrect digits. Check the rules again."
        assert len(remaining_part) == 9, f"Generated number {number} is invalid due to \
    incorrect length. Check the rules again."
        assert remaining_part[0] in ['3', '7'], f"Generated number {number} is invalid \
    due to `{remaining_part[0]}` being first digit after prefix. Check the rules again."
        count_digit[remaining_part[idx_digit]] += 1

    for _, count in count_prefix.items():
        assert abs(count / number_samples - 1/3) < 0.01

    for _, count in count_digit.items():
        assert abs(count / number_samples - 1/10) < 0.01
