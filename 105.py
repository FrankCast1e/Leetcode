'''
@Date: 2020-07-28 16:18:01
@LastEditors: FrankCast1e
@LastEditTime: 2020-07-30 14:30:11
@FilePath: /LeetCode/105.py
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_pos_dict = dict()
        for i in range(len(inorder)):
            inorder_pos_dict[inorder[i]] = i
        root = self.build_tree_with_hash(preorder, inorder, inorder_pos_dict)

        return root
    
    def build_tree_with_hash(self, preorder: List[int], inorder: List[int],index_dict):
        if preorder == inorder == []:
            return None
        root = TreeNode(preorder[0])
        root_index = index_dict[root.val]
        left_inorder = inorder[: root_index]
        right_inorder = inorder[root_index+1: ]

        """
        NOTE:遍历寻找切割点，数量实际上可以根据中序遍历确定。
        i = 1
        while i < len(preorder):
            if preorder[i] not in left_inorder:
                break
            i += 1
        """
        left_tree_node_num = root_index
        left_preorder = preorder[1:1+left_tree_node_num]
        right_preorder = preorder[1+left_tree_node_num:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

x = Solution()
tree = x.buildTree(preorder=[3,9,20,15,7], inorder=[9,3,15,20,7])
print("")