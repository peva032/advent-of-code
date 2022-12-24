import pytest
from advent_of_code.problems.twenty_twentytwo.day_07 import (
    problem_02,
    problem_01,
    FileSystem,
)
import pandas as pd
import pandas.testing as pdt

file_params = [("$ ls", None), ("dir svtswb", None), ("224479 fmfnpm.jqh", 224479)]


@pytest.fixture
def raw_output() -> str:
    # Arrange
    test_output = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k"
    test_dir = {"/": 48381165, "a": 94853, "e": 584, "d": 24933642}
    return test_output, test_dir


@pytest.fixture
def mock_get_input_data(mocker, raw_output) -> None:
    # Arrange input data
    output, _ = raw_output
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_07.get_input_data"
    )
    mocked_func.return_value = output


@pytest.mark.parametrize("line, file_size", file_params)
def test_file_system_get_file_size(line, file_size):
    # Act
    fs = FileSystem()
    output = fs.get_file_size(line)
    # Assert
    assert output == file_size


def test_problem_01(mock_get_input_data):
    # Act
    total_disk_space = problem_01()
    # Assert
    assert total_disk_space == 95437


def test_problem_01(mock_get_input_data):
    # Act
    total_disk_space = problem_02()
    # Assert
    assert total_disk_space == 24933642
