from advent_of_code import DATA_PATH


def get_input_data(year: int, day: int) -> str:
    """Return raw text data for given year and day of month"""

    file_name = f"input_{str(day).zfill(2)}.txt"
    return open(DATA_PATH.joinpath(str(year)).joinpath(file_name), "r").read()
