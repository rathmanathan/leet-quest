import pytest
from study_plans.neetcode_250.arrays_hashing._217_contains_duplicate import Solution

def test_case_1():
    nums = [1, 2, 3, 1]
    assert Solution().containsDuplicate(nums) == True

def test_case_2():
    nums = [1, 2, 3, 4]
    assert Solution().containsDuplicate(nums) == False

def test_case_3():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert Solution().containsDuplicate(nums) == True

def test_case_4():
    nums = []
    assert Solution().containsDuplicate(nums) == False

def test_case_5():
    nums = [1]
    assert Solution().containsDuplicate(nums) == False