from advent_of_code.utils import get_input_data
from typing import List, Tuple
from string import ascii_uppercase, ascii_lowercase


def prepare_input_data() -> List[Tuple[str, str]]:
    rucksack_data = get_input_data(year=2022, day=3).split("\n")
    return [(s[: int(len(s) / 2)], s[int(len(s) / 2) :]) for s in rucksack_data]


def extract_input_data_groups() -> List[Tuple[str, str, str]]:
    rucksack_data = get_input_data(year=2022, day=3).split("\n")
    groups = []
    for i in range(0, len(rucksack_data), 3):
        groups.append(tuple(rucksack_data[i : i + 3]))
    return groups


def get_type_priority(type: str) -> int:
    """
    Returns type priority

    Args:
        type (str): type

    Returns:
        int: priority
    """
    return (
        ascii_uppercase.index(type) + 27
        if type.isupper()
        else ascii_lowercase.index(type) + 1
    )


def problem_01() -> int:
    """
    Prioritise element types

    Returns:
        int: Total prioritsation of rucksack
    """
    rucksack_data = prepare_input_data()
    rucksack_priorition = 0
    for compartment1, compartment2 in rucksack_data:
        s1, s2 = set(compartment1), set(compartment2)
        matched_type = list(s1 & s2)[0]
        char_position = get_type_priority(matched_type)
        rucksack_priorition += char_position
    return rucksack_priorition


def problem_02() -> int:
    """
    Finds common item type in all groups and returns the total
    prioritisation for all groups

    Returns:
        int: total prioritisation
    """
    groups = extract_input_data_groups()
    rucksack_prioritisation = 0
    for group in groups:
        s1, s2, s3 = group
        common_type = list(set(s1) & set(s2) & set(s3))[0]
        rucksack_prioritisation += get_type_priority(common_type)
    return rucksack_prioritisation


if __name__ == "__main__":
    total_priority = problem_01()
    print(total_priority)
    total_group_priority = problem_02()
    print(total_group_priority)
