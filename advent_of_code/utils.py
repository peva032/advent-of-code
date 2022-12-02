from advent_of_code import DATA_PATH


def get_input_data(year: int, day: int, problem_number: int = 1) -> str:
    """Return raw text data for given year and day of month"""
    file_name = f"input_0{problem_number}.txt"
    return open(
        DATA_PATH.joinpath(str(year)).joinpath(str(day)).joinpath(file_name), "r"
    ).read()
