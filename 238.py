'''
Date: 2020-08-11 19:18:02
LastEditors: FrankCast1e
LastEditTime: 2020-08-11 19:28:43
FilePath: /Leetcode/238.py
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        product_sum_forward, product_list_forw = 1, [1]
        product_sum_backward, prodcut_list_backw = 1, [1]
        for i in range(1, len(nums)):
            product_sum_forward = product_sum_forward * nums[i-1]
            product_sum_backward= product_sum_backward * nums[len(nums)-i]
            product_list_forw.append(product_sum_forward)
            prodcut_list_backw.insert(0, product_sum_backward)
        ans = []
        for i in range(len(nums)):
            ans.append(prodcut_list_backw[i]*product_list_forw[i])
        return ans

x = Solution()
print(x.productExceptSelf([1,2,3,4]))