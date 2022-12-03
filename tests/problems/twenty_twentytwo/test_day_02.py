import pytest
from advent_of_code.problems.twenty_twentytwo.day_02 import (
    problem_01,
    prepare_strategy_data,
)


@pytest.fixture
def mock_get_input_data(mocker) -> str:
    # Arrange input data
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_02.get_input_data"
    )
    mocked_func.return_value = "A Y\nB X\nC Z"
    return mocked_func


def test_prepare_strategy_data(mock_get_input_data):
    # Act
    prepared_strategy_data = prepare_strategy_data()
    # Assert
    assert prepared_strategy_data == ["A Y", "B X", "C Z"]


def test_problem_01(mock_get_input_data):
    # Act
    total_score = problem_01()
    # Assert
    assert total_score == 15
