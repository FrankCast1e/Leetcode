'''
Date: 2020-08-10 19:31:10
LastEditors: FrankCast1e
LastEditTime: 2020-08-11 11:39:51
FilePath: /Leetcode/207.py
'''
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 邻接表建立
        neighbour_table = []
        for i in range(numCourses):
            neighbour_table.append([0 for _ in range(numCourses)])
        for request in prerequisites:
            neighbour_table[request[1]][request[0]] = 1
        # 入度表
        in_degree_list = []
        queue = []
        for i in range(numCourses):
            in_degree = 0
            for j in range(numCourses):
                in_degree += neighbour_table[j][i]
            in_degree_list.append(in_degree)
            if in_degree == 0:
                queue.append(i)
        rest_courses_num = numCourses
        while queue != []:
            course = queue.pop(0)
            rest_courses_num -= 1
            for i in range(numCourses):
                if neighbour_table[course][i] == 1:
                    in_degree_list[i] -= 1
                    neighbour_table[course][i] = 0
                    if in_degree_list[i] == 0:
                        queue.append(i)
        if rest_courses_num != 0:
            return False
        else:
            return True

x = Solution()
print(x.canFinish(5, [[1,0],[4,0],[1,2],[4,1],[2,4],[3,4]]))