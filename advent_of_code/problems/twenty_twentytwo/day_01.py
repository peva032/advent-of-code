from advent_of_code.utils import get_input_data
from loguru import logger
from typing import List


def prepare_day_01_data() -> List[int]:
    """
    Load data from file and sum each of the elf's calorie records

    Returns:
        List[int]: Total calories held by each elf
    """
    calorie_data = get_input_data(year=2022, day=1).split("\n\n")
    elf_calorie_data = [sum([int(c) for c in e.split("\n")]) for e in calorie_data]
    logger.info(f"Loaded calorie totals for {len(elf_calorie_data)} elves")
    return elf_calorie_data


def problem_01() -> int:
    """
    Find the elf with the most cals

    Returns:
        int: Max calories held by a single elf
    """
    elf_calorie_data = prepare_day_01_data()
    max_elf_calories = max(elf_calorie_data)
    logger.info(f"The elf with the most calories is carrying {max_elf_calories}cals")
    return max_elf_calories


def problem_02() -> int:
    """
    Find the total calories for the top three elves

    Returns:
        int: Total calories for the top three elves
    """
    elf_calorie_data = prepare_day_01_data()
    elf_calorie_data.sort(reverse=True)

    top_three_elves = elf_calorie_data[:3]
    logger.info(f"Top three elves by calories: {top_three_elves}")

    top_three_calorie_total = sum(top_three_elves)
    logger.info(f"Top three calorie total: {top_three_calorie_total}")

    return top_three_calorie_total


if __name__ == "__main__":
    problem_01()
    problem_02()
