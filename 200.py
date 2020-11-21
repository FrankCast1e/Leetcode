'''
Date: 2020-08-10 17:19:42
LastEditors: FrankCast1e
LastEditTime: 2020-08-10 18:20:14
FilePath: /Leetcode/200.py
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:return 0
        row_num, col_num = len(grid), len(grid[0])
        count = 0
        for i in range(row_num):
            for j in range(col_num):
                area = grid[i][j]
                if area == '1':
                    count += 1
                    self.DFS(grid, i, j)
        return count
                    
    def DFS(self, grid, current_row, current_col):
        if current_row < 0 or current_row >= len(grid) or current_col < 0 or current_col >= len(grid[0]):
            return None
        area = grid[current_row][current_col]
        if area == '0': return None
        else:
            grid[current_row][current_col] = '0'
            self.DFS(grid, current_row+1, current_col)
            self.DFS(grid, current_row-1, current_col)
            self.DFS(grid, current_row, current_col+1)
            self.DFS(grid, current_row, current_col-1)

area_map = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
x = Solution()
print(x.numIslands(area_map))