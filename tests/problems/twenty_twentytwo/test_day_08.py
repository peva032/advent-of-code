import pytest
from advent_of_code.problems.twenty_twentytwo.day_08 import (
    problem_01,
    problem_02,
    prepare_input_data,
    grid_indices,
    visible_to_the_left,
    visible_to_the_right,
    is_visible,
    directional_scenic_score,
    scenic_score,
)
import numpy as np


is_visible_params = [(1, 1, True), (1, 3, False), (2, 3, True), (3, 3, False)]
directional_scenic_score_params = [
    (2, True, 2),
    (0, True, 0),
    (2, False, 1),
    (3, False, 1),
    (4, False, 0),
]
scenic_score_params = [(2, 1, 4), (2, 3, 8)]


@pytest.fixture
def mock_get_input_data(mocker) -> None:
    # Arrange input data
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_08.get_input_data"
    )
    mocked_func.return_value = "30373\n25512\n65332\n33549\n35390"


def test_prepare_input_data(mock_get_input_data):
    # Act
    tree_data = prepare_input_data()
    # Assert
    np.testing.assert_array_equal(
        tree_data,
        np.array(
            [
                [3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0],
            ]
        ),
    )


def test_grid_indices():
    # Arrange
    tree_grid = np.array(
        [
            [3, 0],
            [2, 5],
            [6, 5],
        ]
    )
    excepted_grid_indices = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    # Act
    indices = grid_indices(tree_grid)
    # Assert
    assert indices == excepted_grid_indices


def test_visible_to_the_left():
    # Arrange
    row = [3, 0, 3, 7, 3]
    # Act
    is_visible = visible_to_the_left(row, 2)
    # Assert
    assert is_visible == True


def test_visible_to_the_left_edge():
    # Arrange
    row = [3, 0, 3, 7, 3]
    # Act
    is_visible = visible_to_the_left(row, 0)
    # Assert
    assert is_visible == True


def test_visible_to_the_right():
    # Arrange
    row = [3, 0, 3, 7, 3]
    # Act
    is_visible = visible_to_the_right(row, 2)
    # Assert
    assert is_visible == False


def test_visible_to_the_right_edge():
    # Arrange
    row = [3, 0, 3, 7, 3]
    # Act
    is_visible = visible_to_the_right(row, 4)
    # Assert
    assert is_visible == True


@pytest.mark.parametrize("x,y,visible", is_visible_params)
def test_is_visible(x, y, visible):
    # Arrange
    tree_array = np.array(
        [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
    )
    # Act
    tree_is_visible = is_visible(tree_array, x, y)
    # Assert
    assert tree_is_visible == visible


@pytest.mark.parametrize(
    "position, look_left, expected_score", directional_scenic_score_params
)
def test_directional_scenic_score(position, look_left, expected_score):
    # Arrange
    row = [3, 0, 3, 7, 3]
    # Act
    score = directional_scenic_score(row, position, look_left)
    # Assert
    assert score == expected_score


@pytest.mark.parametrize("x,y,expected_score", scenic_score_params)
def test_scenic_score(x, y, expected_score):
    # Arrange
    tree_array = np.array(
        [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]
    )
    # Act
    tree_score = scenic_score(tree_array, x, y)
    # Assert
    assert tree_score == expected_score


def test_problem_01(mock_get_input_data):
    # Act
    number_of_visible_trees = problem_01()
    # Assert
    assert number_of_visible_trees == 21


def test_problem_02(mock_get_input_data):
    # Act
    best_scenic_score = problem_02()
    # Assert
    assert best_scenic_score == 8
