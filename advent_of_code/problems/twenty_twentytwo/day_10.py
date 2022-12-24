from advent_of_code.utils import get_input_data
from loguru import logger


class CRTSignal:
    def __init__(self, initial_register_value: int = 1) -> None:
        self.signal = [initial_register_value]
        self.cycle = 0
        self.pixels = ["."] * 240

    @property
    def register(self) -> int:
        return self.signal[-1]

    @property
    def sprite(self) -> list:
        x = self.register
        row = int(self.cycle / 40)
        logger.info(row)
        return [x + (40 * row) - 1, self.register + (40 * row), x + (40 * row) + 1]

    def add_x(self, value: int) -> None:
        for cycle in range(2):
            if cycle == 0:
                self.signal.append(self.register)
            else:
                self.signal.append((self.register + int(value)))
            self.cycle += 1
            self.update_crt()

    def noop(self) -> None:
        self.signal.append(self.register)
        self.cycle += 1
        self.update_crt()

    def update_crt(self) -> None:
        if self.cycle in self.sprite:
            logger.info(f"Cycle {self.cycle} intersects the sprite: {self.sprite}")
            self.pixels[self.cycle] = "#"

    def perform_instruction(self, instruction: str) -> None:
        if "addx" in instruction:
            _, value = instruction.split(" ")
            self.add_x(value=value)
        if "noop" in instruction:
            self.noop()

    def get_signal_strength(self, cycle: int) -> int:
        return self.signal[cycle - 1] * cycle

    def draw_crt(self, width: int = 40, height: int = 6) -> None:
        for j in range(height):
            print(" ".join(self.pixels[j * width : (j + 1) * width]))


def problem_01() -> int:
    input_data = get_input_data(year=2022, day=10).splitlines()
    signal = CRTSignal()
    cycles = [20, 60, 100, 140, 180, 220]
    for instruction in input_data:
        signal.perform_instruction(instruction=instruction)
    return sum([signal.get_signal_strength(c) for c in cycles])


def problem_02() -> int:
    input_data = get_input_data(year=2022, day=10).splitlines()
    crt_signal = CRTSignal()
    for instruction in input_data:
        logger.debug(f"Cycle: {crt_signal.cycle}")
        logger.debug(f"Instruction: {instruction}")
        crt_signal.perform_instruction(instruction=instruction)
        logger.info(f"Register: {crt_signal.register}")
    crt_signal.draw_crt()


if __name__ == "__main__":
    # problem_01_value = problem_01()
    # print(problem_01_value)
    problem_02()
