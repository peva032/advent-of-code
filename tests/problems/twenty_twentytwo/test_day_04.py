from advent_of_code.problems.twenty_twentytwo.day_04 import (
    problem_01,
    problem_02,
    prepare_input_data,
)
import pytest


@pytest.fixture
def mock_get_input_data(mocker) -> str:
    # Arrange input data
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_04.get_input_data"
    )
    mocked_func.return_value = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"


def test_prepare_input_data(mock_get_input_data):
    # Act
    pair_sets = prepare_input_data()
    # Assert
    assert pair_sets == [
        ({2, 3, 4}, {6, 7, 8}),
        ({2, 3}, {4, 5}),
        ({5, 6, 7}, {7, 8, 9}),
        ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
        ({6}, {4, 5, 6}),
        ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}),
    ]


def test_problem_01(mock_get_input_data):
    # Act
    number_of_contained_pairs = problem_01()
    # Assert
    assert number_of_contained_pairs == 2


def test_problem_02(mock_get_input_data):
    # Act
    number_of_overlapping_pairs = problem_02()
    # Assert
    assert number_of_overlapping_pairs == 4
