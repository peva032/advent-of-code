from advent_of_code.utils import get_input_data
import numpy as np
from typing import List, Tuple
from loguru import logger


def prepare_input_data() -> np.ndarray:
    """
    Converts raw input data into a numpy array

    Returns:
        np.ndarray: input data represented as a 2D array
    """
    raw_data = get_input_data(year=2022, day=8)
    tree_data = [[int(t) for t in r] for r in raw_data.splitlines()]
    return np.array(tree_data)


def grid_indices(arr: np.ndarray) -> List[Tuple[int, int]]:
    """
    Creates a list of grid indices to loop over

    Args:
        arr (np.ndarray): Input data in array form

    Returns:
        List[Tuple[int, int]]: indices for each tree in grid
    """
    x_len, y_len = arr.shape
    return [(j, i) for j in range(x_len) for i in range(y_len)]


def visible_to_the_left(row: np.ndarray, tree_position: int) -> bool:
    """
    Checks if tree is visible to the left in both row
    or col. If col, then left is equivalent to up

    Args:
        row (np.ndarray): 1D array for tree row or col
        tree_position (int): col or row index (tree position)

    Returns:
        bool: If visible to the left or up
    """
    if tree_position in (0, len(row) - 1):
        logger.info("outside edge, tree is visible")
        return True
    return row[tree_position] > max(row[:tree_position])


def visible_to_the_right(row: np.ndarray, tree_position: int) -> bool:
    """
    Checks if tree is visible to the right in both row
    or col. If col, then right is equivalent to down

    Args:
        row (np.ndarray): 1D array for tree row or col
        tree_position (int): col or row index (tree position)

    Returns:
        bool: Is visible to the right or down
    """
    if tree_position in (0, len(row) - 1):
        logger.info("outside edge, tree is visible")
        return True
    return row[tree_position] > max(row[tree_position + 1 :])


def is_visible(arr: np.ndarray, x: int, y: int) -> bool:
    """
    Checks if tree is visible in all directions

    Args:
        arr (np.ndarray): tree array
        x (int): tree x coord
        y (int): tree y coord

    Returns:
        bool: tree is visible
    """
    row = arr[y, :]
    col = arr[:, x]
    left = visible_to_the_left(row, x)
    right = visible_to_the_right(row, x)
    up = visible_to_the_left(col, y)
    down = visible_to_the_right(col, y)
    return left or right or up or down


def problem_01():
    tree_grid = prepare_input_data()
    tree_indices = grid_indices(arr=tree_grid)
    trees_visible = [1 for x, y in tree_indices if is_visible(tree_grid, x, y)]
    return sum(trees_visible)


def directional_scenic_score(
    row: np.ndarray, tree_position: int, look_left: bool
) -> bool:
    """
    Assess the tree's scenic score to the left or right in both row
    or col. If col, then left is equivalent to up

    Args:
        row (np.ndarray): 1D array for tree row or col
        tree_position (int): col or row index (tree position)
        look_left (bool): if False, looks right/down else left/up

    Returns:
        bool: scenic score in left/up or right/down direction
    """
    scenic_score = 0
    if look_left:
        row_iter = row[:tree_position][::-1]
    else:
        row_iter = row[tree_position + 1 :]

    if tree_position == 0:
        logger.info("outside edge, scenic score 0")
        return scenic_score
    for th in row_iter:
        scenic_score += 1
        if th >= row[tree_position]:
            break
    return scenic_score


def scenic_score(arr: np.ndarray, x: int, y: int) -> int:
    """
    Assesses the scenic score for a tree in all directions

    Args:
        arr (np.ndarray): tree array
        x (int): tree x coord
        y (int): tree y coord

    Returns:
        int: scenic score for tree
    """
    row = arr[y, :]
    col = arr[:, x]
    left = directional_scenic_score(row, x, look_left=True)
    right = directional_scenic_score(row, x, look_left=False)
    up = directional_scenic_score(col, y, look_left=True)
    down = directional_scenic_score(col, y, look_left=False)

    return left * right * up * down


def problem_02():
    tree_grid = prepare_input_data()
    tree_indices = grid_indices(arr=tree_grid)
    tree_scenic_scores = [scenic_score(tree_grid, x, y) for x, y in tree_indices]
    return max(tree_scenic_scores)


if __name__ == "__main__":
    number_of_trees_visible = problem_01()
    print(number_of_trees_visible)
    max_scenic_score = problem_02()
    print(max_scenic_score)
