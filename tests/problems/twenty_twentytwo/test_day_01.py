import pytest
from advent_of_code.problems.twenty_twentytwo.day_01 import (
    prepare_day_01_data,
    problem_01,
    problem_02,
)


@pytest.fixture
def mock_get_input_data(mocker) -> str:
    # Arrange input data
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_01.get_input_data"
    )
    mocked_func.return_value = "5\n5\n\n3\n1\n\n1\n1\n\n2"
    return mocked_func


def test_prepare_day_01_data(mock_get_input_data):
    # Act
    prepared_data = prepare_day_01_data()
    # Assert
    assert prepared_data == [10, 4, 2, 2]


def test_problem_01(mock_get_input_data):
    # Act
    max_elf_calories = problem_01()
    # Assert
    assert max_elf_calories == 10


def test_problem_02(mock_get_input_data):
    # Act
    top_three_total = problem_02()
    # Assert
    assert top_three_total == 16
