import pytest
from study_plans.neetcode_250.arrays_hashing._1929_concatenation_of_array import Solution

def test_case_1():
    nums = [1, 2, 1]
    expected = [1, 2, 1, 1, 2, 1]
    assert Solution().getConcatenation(nums) == expected

def test_case_2():
    nums = [1, 3, 2, 1]
    expected = [1, 3, 2, 1, 1, 3, 2, 1]
    assert Solution().getConcatenation(nums) == expected

def test_case_3():
    nums = [0, 0, 0]
    expected = [0, 0, 0, 0, 0, 0]
    assert Solution().getConcatenation(nums) == expected

def test_case_4():
    nums = []
    expected = []
    assert Solution().getConcatenation(nums) == expected

def test_case_5():
    nums = [1]
    expected = [1, 1]
    assert Solution().getConcatenation(nums) == expected