'''
Date: 2020-08-11 19:34:51
LastEditors: FrankCast1e
LastEditTime: 2020-08-12 09:06:29
FilePath: /Leetcode/240.py
'''
# 时间复杂度过高
"""
class Solution:
    def searchMatrix(self, matrix, target):
"""
        #:type matrix: List[List[int]]
        #:type target: int
        #:rtype: bool
"""
        if matrix == []:
            return False
        result = self.BFS(matrix, target, 0, 0)
        return result
        
    def BFS(self, matrix, target, i, j):
        if i >= len(matrix) or j >= len(matrix[0]):
            return False
        if matrix[i][j] > target:
            return False
        if matrix[i][j] == target:
            return True
        res1 = self.BFS(matrix, target, i+1, j)
        res2 = self.BFS(matrix, target, i, j+1)
        return res1 or res2
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

x = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(x.searchMatrix(matrix, 20))