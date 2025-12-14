import pytest
from solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        pytest.param([2, 7, 11, 15], 9, [0, 1], id="1"),
        pytest.param([3, 2, 4], 6, [1, 2], id="2"),
        pytest.param([3, 3], 6, [0, 1], id="3"),
        pytest.param([1, 2], 3, [0, 1], id="4"),
        pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19, [8, 9], id="5"),
        pytest.param([-3, 5, -10, 3, -2], -7, [2, 3], id="6"),
        pytest.param([1, 4, 10, -3], 1, [1, 3], id="7"),
        pytest.param([-1, -2, -3, -4, -5], -8, [2, 4], id="8"),
        pytest.param([0, 0], 0, [0, 1], id="9"),
        pytest.param([1000000000, -1000000000], 0, [0, 1], id="10"),
    ],
)
def test(solution, nums, target, expected):
    result = solution.twoSum(nums.copy(), target)
    assert (
        result == expected
    ), f"nums={nums} target={target} expected={expected} got={result}"
