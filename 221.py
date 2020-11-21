'''
Date: 2020-08-11 14:10:27
LastEditors: FrankCast1e
LastEditTime: 2020-08-11 15:07:28
FilePath: /Leetcode/221.py
'''
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        row_num, col_num = len(matrix), len(matrix[0])
        max_len = 0
        for i in range(row_num):
            for j in range(col_num):
                if matrix[i][j] == "1":
                    max_len_point = 1+self.maxSquareFromPoint(matrix,i,j)
                    if max_len_point > max_len:
                        max_len = max_len_point
        return max_len*max_len

    def maxSquareFromPoint(self, matrix, row_id, col_id):
        i = 1
        while row_id+i < len(matrix) and col_id+i < len(matrix[0]):
            shit = False
            for pos in range(i+1):
                right_side = matrix[row_id+pos][col_id+i]
                left_side = matrix[row_id+i][col_id+pos]
                if right_side != "1" or left_side != "1":
                    shit = True
            if shit: break
            else:
                i += 1
        return i-1

x = Solution()
matrix = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]
print(x.maximalSquare(matrix))