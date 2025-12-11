"""Module in sub_folder_2."""

from src.sub_folder_1.test1 import calculate


def double_calculate(a: int, b: int) -> int:
    return calculate(a, b) * 2
