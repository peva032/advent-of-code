import pytest
from advent_of_code.problems.twenty_twentytwo.day_06 import (
    start_of_packet_marker,
)


params = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4, 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14, 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 14, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 14, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14, 26),
]


@pytest.mark.parametrize("input, distinct_characters, expected_output", params)
def test_start_of_packet_marker(input, distinct_characters, expected_output):
    # Act
    marker = start_of_packet_marker(input, distinct_chars=distinct_characters)
    # Assert
    assert marker == expected_output
