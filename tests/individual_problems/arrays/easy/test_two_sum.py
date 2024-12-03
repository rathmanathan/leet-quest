import unittest
import pytest

from individual_problems.arrays.easy._001_two_sum import Solution

def test_case_1():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [1, 0]
    assert Solution().twoSum(nums, target) == expected
