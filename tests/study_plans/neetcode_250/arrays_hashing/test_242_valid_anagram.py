import pytest
from study_plans.neetcode_250.arrays_hashing._242_valid_anagram import Solution

def test_case_1():
    s = "anagram"
    t = "nagaram"
    assert Solution().isAnagram(s, t) == True

def test_case_2():
    s = "rat"
    t = "car"
    assert Solution().isAnagram(s, t) == False

def test_case_3():
    s = "a"
    t = "a"
    assert Solution().isAnagram(s, t) == True

def test_case_4():
    s = "ab"
    t = "ba"
    assert Solution().isAnagram(s, t) == True

def test_case_5():
    s = "abcd"
    t = "abc"
    assert Solution().isAnagram(s, t) == False