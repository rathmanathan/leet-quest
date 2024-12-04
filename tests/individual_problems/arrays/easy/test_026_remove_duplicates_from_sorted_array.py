import pytest

from individual_problems.arrays.easy._026_remove_duplicates_from_sorted_array import Solution

def test_use_case_01():
    nums = [1,1,2]
    output = 2
    output_nums = [1,2,2]
    solution = Solution()
    result = solution.removeDuplicates(nums)
    assert result == output
