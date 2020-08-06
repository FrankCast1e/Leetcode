'''
@Date: 2020-07-31 14:45:03
@LastEditors: FrankCast1e
@LastEditTime: 2020-07-31 15:26:12
@FilePath: /LeetCode/96.py
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def numTrees(self, n: int) -> int:
#         nums = [i+1 for i in range(n)]
#         all_num = self.build_search_tree(nums)
#         return all_num

#     def build_search_tree(self, nums):
#         if nums == []:
#             return 1
#         count = 0
#         for i in range(len(nums)):
#             left_count = self.build_search_tree(nums[:i])
#             right_count = self.build_search_tree(nums[i+1:])
#             count += left_count*right_count
#         return count

# Catalan Number
class Solution:
    def numTrees(self, n: int) -> int:
        memo = []
        memo.append(1)
        memo.append(1)
        for i in range(2,n+1):
            g_n = 0
            for j in range(i):
                g_n += memo[j]*memo[i-1-j]
            memo.append(g_n)
        return memo[-1]

x = Solution()
print(x.numTrees(4))