from advent_of_code.utils import get_input_data
from typing import List, Tuple


def prepare_input_data() -> List[Tuple[set, set]]:
    input_data = get_input_data(year=2022, day=4).splitlines()
    pairs = [tuple(l.split(",")) for l in input_data]
    pair_ranges = [(p[0].split("-"), p[1].split("-")) for p in pairs]
    pair_sets = [
        (set(range(int(r1[0]), int(r1[1]) + 1)), set(range(int(r2[0]), int(r2[1]) + 1)))
        for r1, r2 in pair_ranges
    ]
    return pair_sets


def problem_01() -> int:
    """
    Finds the total number of pairs that have one pair fully
    contained by the other

    Returns:
        int: count of fully contained pairs
    """
    pair_sets = prepare_input_data()
    is_contained = [s1.issubset(s2) or s2.issubset(s1) for s1, s2 in pair_sets]
    return sum(is_contained)


def problem_02() -> int:
    """
    Finds the total number of pairs that have an overlap

    Returns:
        int: count of pairs with overlap
    """
    pair_sets = prepare_input_data()
    is_contained = [1 if s1.intersection(s2) else 0 for s1, s2 in pair_sets]
    return sum(is_contained)


if __name__ == "__main__":
    pairs_fully_contained = problem_01()
    print(pairs_fully_contained)
    pairs_with_overlap = problem_02()
    print(pairs_with_overlap)
