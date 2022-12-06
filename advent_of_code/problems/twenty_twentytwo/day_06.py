from advent_of_code.utils import get_input_data
from loguru import logger


def start_of_packet_marker(packet: str, distinct_chars: int) -> int:
    """
    Subroutine to identify start of signal marker

    Args:
        packet (str): signal packet
        distinct_chars (int): distinct number of consecutive characters

    Returns:
        int: start of signal marker position
    """
    marker = None
    for ind in range(len(packet)):
        check_substr = set(packet[ind : ind + distinct_chars])
        if len(check_substr) == distinct_chars:
            logger.info(f"Found unique substring {check_substr} at {ind}")
            marker = ind + distinct_chars
            logger.info(f"Signal marker found at: {marker}")
            return marker
    raise Exception(f"Marker not found for packet: {packet}")


def problem_01(packet: str) -> int:
    """
    Runs start of packet marker subroutine to identify
    start of signal, with 4 consecutive unique characters

    Args:
        packet (str): Signal

    Returns:
        int: marker
    """
    return start_of_packet_marker(packet=packet, distinct_chars=4)


def problem_02(packet: str) -> int:
    """
    Runs start of packet marker subroutine to identify
    start of signal, with 14 consecutive unique characters

    Args:
        packet (str): Signal

    Returns:
        int: marker
    """
    return start_of_packet_marker(packet=packet, distinct_chars=14)


if __name__ == "__main__":
    packet = get_input_data(year=2022, day=6)
    problem_01(packet=packet)
    problem_02(packet=packet)
