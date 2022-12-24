import pandas as pd
from advent_of_code.utils import get_input_data
from loguru import logger
from typing import List, Union


class FileSystem:
    def __init__(self, filesize_limit: int = 100000) -> None:
        self.filesize_limit = filesize_limit
        self.dir_paths = [""]
        self.dirs = {}

    @property
    def current_dir(self) -> str:
        return self.dir_paths[-1]

    @property
    def parent_dir(self) -> str:
        return self.dir_paths[-2] if len(self.dir_paths) > 1 else ""

    @property
    def path(self) -> str:
        return "/".join(self.dir_paths)

    def get_file_size(self, line: str) -> int:
        split_line = line.split(" ")
        if split_line[0].isnumeric():
            return int(split_line[0])
        logger.debug(f"line is not a file")

    def change_dir(self, line: str) -> None:
        split_line = line.split(" ")
        if split_line[1] == "cd":
            origin = self.current_dir
            destination = split_line[2]
            if destination == "..":
                new_dir = self.dir_paths.pop()
                logger.debug(f"Moving up to parent directory {new_dir}")
            else:
                new_dir = self.path + "/" + destination
                self.dir_paths.append(new_dir)
            logger.info(f"Change directory from {origin} to {new_dir}")

    def update_dir_sizes(self, file_size: int) -> None:
        for dir_path in self.dir_paths:
            self.dirs[dir_path] = self.dirs.get(dir_path, 0) + file_size

    def read_line(self, line: str) -> None:
        self.change_dir(line)
        file_size = self.get_file_size(line)
        if file_size:
            logger.info(f"Updating file system directory sizes")
            self.update_dir_sizes(file_size)

    def get_total_dir_file_size(self) -> int:
        return sum([v for v in self.dirs.values() if v <= self.filesize_limit])

    def free_space(self, file_system_size: int = 70000000) -> int:
        return file_system_size - self.dirs.get("", 0)

    def get_dir_for_deletion(self, free_space_requirement: int) -> int:
        dirs_over_requirement = [
            v for v in self.dirs.values() if v >= free_space_requirement
        ]
        return min(dirs_over_requirement)


def problem_01() -> int:
    input_data = get_input_data(year=2022, day=7).splitlines()
    fs = FileSystem()
    for line in input_data:
        fs.read_line(line)
    return fs.get_total_dir_file_size()


def problem_02() -> int:
    input_data = get_input_data(year=2022, day=7).splitlines()
    fs = FileSystem()
    for line in input_data:
        fs.read_line(line)
    free_space = fs.free_space()
    required_space = 30000000 - free_space
    return fs.get_dir_for_deletion(required_space)


if __name__ == "__main__":
    problem_one_size = problem_01()
    print(problem_one_size)
    problem_two_size = problem_02()
    print(problem_two_size)
