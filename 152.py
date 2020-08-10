'''
Date: 2020-08-10 10:47:43
LastEditors: FrankCast1e
LastEditTime: 2020-08-10 11:43:54
FilePath: /Leetcode/152.py
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        description: 动态规划，和53题【最大子序和】类似。但是，需要注意是否满足最优子结构。
                    由于存在负数，所以需要保存当前的最小值，最小值搞不好乘个负数就变成了最大值。
                    f_max：以当前位置结尾的子数组，乘积最大值
                    f_min：以当前位置结尾的子数组，乘积最小值
        param {type} 
        return {type} 
        '''
        ans = nums[0]
        f_max, f_min = nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            candidate1 = f_max*num
            candidate2 = f_min*num
            candidate3 = num
            f_max = max(candidate1, candidate2, candidate3)
            f_min = min(candidate1, candidate2, candidate3)
            if f_max > ans:
                ans = f_max
        return ans

x = Solution()
print(x.maxProduct([2,3,-2,4,-2]))