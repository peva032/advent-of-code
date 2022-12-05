import re
from typing import Dict, List, Tuple

from advent_of_code.utils import get_input_data
from loguru import logger


def split_input_data() -> Tuple[str, str]:
    """
    Splits input data into stack and instructions

    Returns:
        Tuple[str, str]: stack, instructions
    """
    input_data = get_input_data(year=2022, day=5)
    input_data_parts = tuple(input_data.split("\n\n"))
    return input_data_parts


def get_stack_numbers(stack: str) -> List[str]:
    """
    Gets the stack numbers as indexes for each stack

    Args:
        stack (str): string representing full stack diagram

    Returns:
        List[str]: list of individual stack identifiers
    """
    stack_rows = stack.splitlines()
    # Stack numbers are in the last column of the stack
    return stack_rows[-1].strip().split("   ")


def extract_stack_row(stack_row: str) -> str:
    """
    Extracts each stack row

    Args:
        stack (str): string represtenting full stack diagram

    Returns:
        str: string representing row without diagram characters
    """
    return (
        stack_row.replace("    ", "[.]")
        .replace("] [", "")
        .replace("[", "")
        .replace("]", "")
        .replace(".", " ")
    )


def populate_stack(stack_dict: dict, stack_row: str) -> None:
    """
    Populates stack dictionary with row of containers

    Args:
        stack_dict (dict): Dictionary representation of stack
        stack_row (str): basic string representation of stack row
    """
    for ind, c in enumerate(extract_stack_row(stack_row)):
        if c != " ":
            stack_dict[str(ind + 1)] += c
        else:
            logger.info(f"No container in row {ind}")


def prepare_stack(stack: str) -> Dict[str, str]:
    """
    Converts string stack into dictionary

    Args:
        stack: string representation of stack

    Returns:
        Dict[str, str]: dictionary representation of stack
    """
    keys = get_stack_numbers(stack=stack)
    stack_dict = {k: "" for k in keys}
    stack_rows = stack.splitlines()[:-1]
    stack_rows.reverse()
    for ind, row in enumerate(stack_rows):
        logger.info(f"populating stack row: {ind}")
        populate_stack(stack_dict, row)
    return stack_dict


def perform_crane_instructions_9000(stack_dict: dict, instruction: str) -> None:
    """
    Interprets and performs raw text instructions with the 9000 model crane

    Args:
        stack_dict (dict): dictionary representation of stack
        instruction (str): Crane move instruction
    """
    number_of_containers, origin, destination = tuple(re.findall(r"\d+", instruction))
    for i in range(int(number_of_containers)):
        container = stack_dict[origin][-1]
        stack_dict[origin] = stack_dict[origin][:-1]
        logger.info(f"Moving {container} from {origin} to {destination}")
        stack_dict[destination] += container


def perform_crane_instructions_9001(stack_dict: dict, instruction: str) -> None:
    """
    Interprets and performs raw text instructions with the 9001 model crane
    that can move more than one container at a time.

    Args:
        stack_dict (dict): dictionary representation of stack
        instruction (str): Crane move instruction
    """
    number_of_containers, origin, destination = tuple(re.findall(r"\d+", instruction))
    containers = stack_dict[origin][-int(number_of_containers) :]
    stack_dict[origin] = stack_dict[origin][: -int(number_of_containers)]
    logger.info(f"Moving {containers} from {origin} to {destination}")
    stack_dict[destination] += containers


def get_top_layer(stack: dict) -> str:
    """
    Returns top layer of containers on stack

    Args:
        stack (dict): dictionary representation of stack

    Returns:
        str: top layer of containers
    """
    top_layer = ""
    for k, v in stack.items():
        top_container = v[-1] if v else " "
        logger.info(f"Container: [{top_container}] is at the top of stack {k}")
        top_layer += top_container
    return top_layer


def problem_01() -> str:
    """
    Takes a set of instructions for moving containers on a stack
    and returns the a string representing the top layer of containers

    Returns:
        str: top layer of containers
    """
    # Prepare the input data
    stack_raw, instructions_raw = split_input_data()
    stack = prepare_stack(stack=stack_raw)
    instructions = instructions_raw.splitlines()

    # Perform crane instructions
    for instruction in instructions:
        perform_crane_instructions_9000(stack_dict=stack, instruction=instruction)

    # Read out top layer of containers
    print(stack)
    return get_top_layer(stack=stack)


def problem_02() -> str:
    """
    Takes a set of instructions for moving containers (Using 9001 model crane
    that can move more than one container at a time) on a stack and returns
    the a string representing the top layer of containers

    Returns:
        str: top layer of containers
    """
    # Prepare the input data
    stack_raw, instructions_raw = split_input_data()
    stack = prepare_stack(stack=stack_raw)
    instructions = instructions_raw.splitlines()

    # Perform crane instructions
    for instruction in instructions:
        perform_crane_instructions_9001(stack_dict=stack, instruction=instruction)

    # Read out top layer of containers
    print(stack)
    return get_top_layer(stack=stack)


if __name__ == "__main__":
    top_layer_01 = problem_01()
    print(top_layer_01)
    top_layer_02 = problem_02()
    print(top_layer_02)
