import pytest
from advent_of_code.problems.twenty_twentytwo.day_11 import (
    problem_01,
    problem_02,
    Monkey,
)


@pytest.fixture
def mock_get_input_data_01(mocker) -> None:
    # Arrange input data
    mocked_func = mocker.patch(
        "advent_of_code.problems.twenty_twentytwo.day_11.get_input_data"
    )
    mocked_func.return_value = "Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3\n\nMonkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0\n\nMonkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3\n\nMonkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1"


def test_monkey_parse():
    # Arrange
    raw_monkey = "Monkey 0:\n    Starting items: 79, 98\n    Operation: new = old * 19\n    Test: divisible by 23\n        If true: throw to monkey 2\n        If false: throw to monkey 3"
    monkey_0 = Monkey(monkey_str=raw_monkey)
    # Act
    monkey_0.parse()
    # Assert
    assert monkey_0.name == "Monkey 0"
    assert monkey_0.items == [79, 98]
    assert monkey_0.operator == "*"
    assert monkey_0.operator_value == "19"
    assert monkey_0.test_divisor == 23
    assert monkey_0.test_is_true == "2"
    assert monkey_0.test_is_false == "3"


def test_problem_01(mock_get_input_data_01):
    # Act
    output = problem_01()
    # Assert
    assert output == 10605


def test_problem_02(mock_get_input_data_01):
    # Act
    output = problem_02()
    # Assert
    assert output == 2713310158
