# Leetcode Problem : https://leetcode.com/problems/concatenation-of-array/description/

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * (n * 2)
        for i in range(n):
            ret[i] = nums[i]
            ret[i + n] = nums[i]
        return ret
    
if __name__ == "__main__":
    print(Solution().getConcatenation([1,2,1]))
    print(Solution().getConcatenation([1,3,2,1]))