from advent_of_code.utils import get_input_data
from loguru import logger
import math


class Monkey:
    def __init__(self, monkey_str: str) -> None:
        self.monkey_str = monkey_str
        self.name = None
        self.items = []
        self.operator = None
        self.operator_value = None
        self.test_divisor = None
        self.test_is_true = None
        self.test_is_false = None
        self.inspections = 0

    def parse(self) -> None:
        """
        Parses raw string monkey attributes into class attrs
        """
        (
            name,
            starting_items,
            operation,
            condition,
            iftrue,
            iffalse,
        ) = self.monkey_str.splitlines()
        self.name = name[:-1]
        self.items = [int(i) for i in starting_items.split(":")[1].split(",")]
        self.operator = operation.split("= ")[1][4:].split(" ")[0]
        self.operator_value = operation.split("= ")[1][4:].split(" ")[1]
        self.test_divisor = int(
            condition.split(":")[1].strip().split("divisible by ")[1]
        )
        self.test_is_true = iftrue.split(":")[1].strip().split("throw to monkey ")[1]
        self.test_is_false = iffalse.split(":")[1].strip().split("throw to monkey ")[1]


class MonkeyInTheMiddle:
    def __init__(
        self, monkeys: str, rounds: int = 20, use_mod_all: bool = False
    ) -> None:
        self.monkeys = monkeys
        self.rounds = rounds
        self.monkey_group = {}
        self.mod_all = 1
        self.use_mod_all = use_mod_all

    def parse_monkey_group(self) -> None:
        """
        Parses input monkey data and populatest the group of Monkey dictionary
        """
        for monkey in self.monkeys.split("\n\n"):
            m = Monkey(monkey)
            m.parse()
            self.monkey_group[m.name] = m
            self.mod_all *= m.test_divisor

    def monkey_decision(self, monkey: Monkey, worry_level: int) -> None:
        """
        Pass the item to another monkey based on worry level

        Args:
            monkey (Monkey): Monkey with item
            worry_level (int): worry level after assessing the item
        """
        test = worry_level % monkey.test_divisor == 0
        if test:
            throw_to = "Monkey " + monkey.test_is_true
        else:
            throw_to = "Monkey " + monkey.test_is_false
        # Throw item with update worry level to new monkey
        self.monkey_group[throw_to].items.append(worry_level)

    def monkey_inspection(self, monkey: Monkey) -> None:
        """
        Performs a single monkey inspection of all items
        """
        # logger.info(f"{monkey.name} is inspecting its items")
        for item in monkey.items:
            # Assess worry level
            monkey.inspections += 1
            if monkey.operator_value == "old":
                value = item
            else:
                value = int(monkey.operator_value)
            if monkey.operator == "+":
                new = item + value
            elif monkey.operator == "*":
                new = item * value
            # Worry level relief
            if self.use_mod_all:
                new = new % self.mod_all
            else:
                new = int(new / 3)
            self.monkey_decision(monkey=monkey, worry_level=new)

        monkey.items = []

    def play_round(self) -> None:
        """
        Plays one round of Monkey in the middle
        """
        for monkey in self.monkey_group.values():
            self.monkey_inspection(monkey=monkey)

    def play_game(self) -> None:
        """
        Plays full game of Monkey in the middle
        """
        for i in range(self.rounds):
            self.play_round()
            if (i + 1) in [1, 20] or (i + 1) % 1000 == 0:
                self.round_summary(round_number=i + 1)

    def top_monkeys(self, number_of_monkeys: int = 2) -> int:
        """
        Returns the number of inspections of the top monkeys multiplied together

        Args:
            number_of_monkeys (int, optional): number of top monkeys. Defaults to 2.

        Returns:
            int: top monkey inspection numbers multiplied together
        """
        val = 1
        inspections = [m.inspections for m in self.monkey_group.values()]
        inspections.sort()
        for i in inspections[-number_of_monkeys:]:
            val *= i
        return val

    def round_summary(self, round_number: int) -> None:
        """
        Prints out round summary

        Args:
            round_number (int): round number
        """
        print(f"== After round {round_number} ==")
        for monkey in self.monkey_group.values():
            print(f"{monkey.name} inspected items {monkey.inspections} times")


def problem_01() -> int:
    monkey_info = get_input_data(year=2022, day=11)
    mitm = MonkeyInTheMiddle(monkeys=monkey_info)
    mitm.parse_monkey_group()
    mitm.play_game()
    return mitm.top_monkeys()


def problem_02():
    monkey_info = get_input_data(year=2022, day=11)
    mitm = MonkeyInTheMiddle(monkeys=monkey_info, rounds=10000, use_mod_all=True)
    mitm.parse_monkey_group()
    mitm.play_game()
    return mitm.top_monkeys()


if __name__ == "__main__":
    # problem_01_value = problem_01()
    # print(problem_01_value)
    problem_02_value = problem_02()
    print(problem_02_value)
