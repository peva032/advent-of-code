from advent_of_code.utils import get_input_data
from typing import List, Tuple
from loguru import logger


def prepare_strategy_data() -> List[Tuple[str, str]]:
    """
    Prepare input data into list of tuples for each round

    Returns:
        List[Tuple[str, str]]: list of tuples for each round
    """
    strategy_data = get_input_data(year=2022, day=2).splitlines()
    logger.info(f"Loaded strategies for {len(strategy_data)} rounds")
    return strategy_data


def problem_01() -> int:
    """
    Day 2 problem 01: Calculates total score for strategy
    data

    Returns:
        int: total score
    """
    selection_lookup = {"X": 1, "Y": 2, "Z": 3}
    outcome_pairs = {
        "A X": 3,
        "B Y": 3,
        "C Z": 3,
        "A Y": 6,
        "B Z": 6,
        "C X": 6,
        "A Z": 0,
        "B X": 0,
        "C Y": 0,
    }

    strategy_data = prepare_strategy_data()
    round_scores = []

    for round in strategy_data:
        _, strategy = round.split(" ")
        score = outcome_pairs[round] + selection_lookup[strategy]
        round_scores.append(score)
    return sum(round_scores)


def problem_02() -> int:
    """
    Day 2 problem 02: Calculates total score with pre-defined strategy

    Returns:
        int: total score
    """
    outcome_lookup = {"X": 0, "Y": 3, "Z": 6}
    selection_lookup = {
        "A X": 3,
        "B X": 1,
        "C X": 2,
        "A Y": 1,
        "B Y": 2,
        "C Y": 3,
        "A Z": 2,
        "B Z": 3,
        "C Z": 1,
    }

    strategy_data = prepare_strategy_data()
    round_scores = []

    for round in strategy_data:
        _, strategy = round.split(" ")
        score = selection_lookup[round] + outcome_lookup[strategy]
        round_scores.append(score)

    return sum(round_scores)


if __name__ == "__main__":
    problem_one_total_score = problem_01()
    logger.info(problem_one_total_score)
    problem_two_total_score = problem_02()
    logger.info(problem_two_total_score)
