'''
Date: 2020-08-11 15:20:40
LastEditors: FrankCast1e
LastEditTime: 2020-08-11 19:13:37
FilePath: /Leetcode/236.py
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        _,_, x = self.DFS(root, p, q)
        return x
        
    def DFS(self, root, p, q):
        if root == None:
            return False, False, None

        if root.val == p:
            p_available_root = True
        else:
            p_available_root = False
        if root.val == q:
            q_available_root = True
        else:
            q_available_root = False
        
        p_available_left, q_available_left, common_ancestor_left = self.DFS(root.left, p, q)
        if common_ancestor_left != None:
            return True, True, common_ancestor_left
        p_available_right, q_available_right, common_ancestor_right = self.DFS(root.right, p, q)
        if common_ancestor_right != None:
            return True, True, common_ancestor_right
        
        p_available = p_available_root or p_available_left or p_available_right
        q_available = q_available_root or q_available_left or q_available_right
        
        if p_available and q_available:
            return True, True, root
        elif p_available:
            return True, False, None
        elif q_available:
            return False, True, None
        else:
            return False, False, None

from utils import create_BinaryTree_from_list
x = Solution()
root = create_BinaryTree_from_list([3,5,1,6,2,0,8,'null','null',7,4])
node = x.lowestCommonAncestor(root, 5, 4)
print(node.val)