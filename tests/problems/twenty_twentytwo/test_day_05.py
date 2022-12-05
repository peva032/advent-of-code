import pytest
from advent_of_code.problems.twenty_twentytwo.day_05 import (
    problem_01,
    problem_02,
    split_input_data,
    get_stack_numbers,
    extract_stack_row,
    populate_stack,
    prepare_stack,
    get_top_layer,
    perform_crane_instructions_9000,
    perform_crane_instructions_9001,
)

extract_stack_row_params = [
    ("one_missing", "[S] [W] [H]     [B] [H] [D] [C] [M]", "SWH BHDCM"),
    ("two_missing", "[S] [W] [H]         [H] [D] [C] [M]", "SWH  HDCM"),
    ("none_missing", "[S] [W] [H] [A] [C] [B] [H] [D] [C] [M]", "SWHACBHDCM"),
]


@pytest.fixture
def mock_get_input_data(mocker) -> str:
    # Arrange input data
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_05.get_input_data"
    )
    mocked_func.return_value = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2\n"


def test_split_input_data(mock_get_input_data):
    # Act
    parts = split_input_data()
    # Assert
    assert parts == (
        "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 ",
        "move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2\n",
    )


def test_get_stack_numbers(mock_get_input_data):
    # Arrange
    stack, _ = split_input_data()
    # Act
    stack_numbers = get_stack_numbers(stack=stack)
    # Assert
    assert stack_numbers == ["1", "2", "3"]


@pytest.mark.parametrize("case,input,expected_output", extract_stack_row_params)
def test_extract_stack_row(case, input, expected_output):
    # Act
    extracted_stack_row = extract_stack_row(stack_row=input)
    # Assert
    assert extracted_stack_row == expected_output


def test_populate_stack():
    # Arrange
    stack_dict = {str(k + 1): "" for k in range(9)}
    # Act
    populate_stack(stack_dict=stack_dict, stack_row="SWH BHDCM")
    # Assert
    assert stack_dict == {
        "1": "S",
        "2": "W",
        "3": "H",
        "4": "",
        "5": "B",
        "6": "H",
        "7": "D",
        "8": "C",
        "9": "M",
    }


def test_prepare_stack(mock_get_input_data):
    # Arrange
    stack, _ = split_input_data()
    # Act
    stack_dict = prepare_stack(stack=stack)
    # Assert
    assert stack_dict == {"1": "ZN", "2": "MCD", "3": "P"}


def test_perform_crane_instruction_9000():
    # Arrange
    stack_dict = {"1": "AZ", "2": "BD", "3": "C"}
    crane_instruction = "move 2 from 1 to 3"
    # Act
    perform_crane_instructions_9000(
        stack_dict=stack_dict, instruction=crane_instruction
    )
    # Assert
    assert stack_dict == {"1": "", "2": "BD", "3": "CZA"}


def test_perform_crane_instruction_9001():
    # Arrange
    stack_dict = {"1": "AZ", "2": "BD", "3": "C"}
    crane_instruction = "move 2 from 1 to 3"
    # Act
    perform_crane_instructions_9001(
        stack_dict=stack_dict, instruction=crane_instruction
    )
    # Assert
    assert stack_dict == {"1": "", "2": "BD", "3": "CAZ"}


def test_get_top_layer():
    # Arrange
    stack = {"1": "", "2": "BD", "3": "CZA"}
    # Act
    top_layer = get_top_layer(stack=stack)
    # Assert
    assert top_layer == " DA"


def test_problem_01(mock_get_input_data):
    # Act
    top_containers = problem_01()
    # Assert
    assert top_containers == "CMZ"


def test_problem_02(mock_get_input_data):
    # Act
    top_containers = problem_02()
    # Assert
    assert top_containers == "MCD"
