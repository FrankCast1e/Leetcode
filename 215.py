'''
Date: 2020-08-11 12:17:00
LastEditors: FrankCast1e
LastEditTime: 2020-08-11 14:08:02
FilePath: /Leetcode/215.py
'''
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

x = Solution()
print(x.findKthLargest([3,2,3,1,2,4,5,5,6], 4))