'''
Date: 2020-08-13 09:49:01
LastEditors: FrankCast1e
LastEditTime: 2020-08-13 10:08:53
FilePath: /Leetcode/279.py
'''

class Solution:
    def numSquares(self, n: int) -> int:
        min_squares = [0,1]
        if n == 0:
            return 0
        for i in range(1,n):
            num = i + 1
            candidate = []
            possible_square = 1
            while num - possible_square**2 >= 0:
                candidate.append(min_squares[num-possible_square**2]+1)
                possible_square += 1
            min_squares.append(min(candidate))
        return min_squares[-1]
    
x = Solution()
print(x.numSquares(1))