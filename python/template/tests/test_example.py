"""Example tests."""

from src.utils import add
from src.sub_folder_1.test1 import calculate
from src.sub_folder_2.test2 import double_calculate


def test_add():
    assert add(2, 3) == 5


def test_calculate():
    assert calculate(2, 3) == 5


def test_double_calculate():
    assert double_calculate(2, 3) == 10
