import unittest
import pytest

from individual_problems.arrays.easy._001_two_sum import Solution

def test_case_1():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert Solution().twoSum(nums, target) == expected

def test_case_2():
    nums = [3,2,4]
    target = 6
    expected = [1, 2]
    assert Solution().twoSum(nums, target) == expected
    
def test_case_3():
    nums = [3,3]
    target = 6
    expected = [0, 1]
    assert Solution().twoSum(nums, target) == expected