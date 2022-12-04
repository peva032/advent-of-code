import pytest
from advent_of_code.problems.twenty_twentytwo.day_03 import (
    problem_01,
    problem_02,
    get_type_priority,
    prepare_input_data,
    extract_input_data_groups,
)


params = [("lowercase", "p", 16), ("uppercase", "L", 38)]


@pytest.fixture
def mock_get_input_data(mocker) -> str:
    # Arrange input data
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_03.get_input_data"
    )
    mocked_func.return_value = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"


@pytest.fixture
def mock_get_input_data_for_prep(mocker) -> str:
    # Arrange input data for preparation test
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_03.get_input_data"
    )
    mocked_func.return_value = "vJrwpWtwJgWrhcsFMMfFFhFp"


def test_prepare_input_data(mock_get_input_data_for_prep):
    # Arrange
    prepared_data = prepare_input_data()
    # Assert
    assert prepared_data == [("vJrwpWtwJgWr", "hcsFMMfFFhFp")]


def test_extract_input_data_groups(mock_get_input_data):
    # Act
    groups = extract_input_data_groups()
    # Assert
    assert groups[0] == (
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    )


@pytest.mark.parametrize("case,type,expected_priority", params)
def test_get_type_priority(case, type, expected_priority):
    # Act
    priority = get_type_priority(type=type)
    # Assert
    assert expected_priority == priority


def test_problem_01(mock_get_input_data):
    # Act
    total_prioritisation = problem_01()
    # Assert
    assert total_prioritisation == 157


def test_problem_02(mock_get_input_data):
    # Act
    total_prioritisation = problem_02()
    # Assert
    assert total_prioritisation == 70
