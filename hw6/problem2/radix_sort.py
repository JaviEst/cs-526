from typing import List

BASE = 10


def radix_sort(arr: List[int]) -> List[int]:
    if not arr:
        return []

    positives = [value for value in arr if value >= 0]
    negatives = [-value for value in arr if value < 0]

    sorted_positives = _lsd_radix(positives) if positives else []
    sorted_negatives = _lsd_radix(negatives) if negatives else []

    sorted_negatives = [-value for value in reversed(sorted_negatives)]

    return sorted_negatives + sorted_positives


def _lsd_radix(values: List[int]) -> List[int]:
    if not values:
        return []

    result = values[:]
    max_value = max(values)
    exp = 1

    while max_value // exp > 0:
        result = _counting_sort_by_digit(result, exp)
        exp *= BASE

    return result


def _counting_sort_by_digit(values: List[int], exp: int) -> List[int]:
    count = [0] * BASE
    output = [0] * len(values)

    for value in values:
        digit = (value // exp) % BASE
        count[digit] += 1

    for i in range(1, BASE):
        count[i] += count[i - 1]

    for value in reversed(values):
        digit = (value // exp) % BASE
        count[digit] -= 1
        output[count[digit]] = value

    return output
