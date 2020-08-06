'''
@Date: 2020-07-30 14:27:47
@LastEditors: FrankCast1e
@LastEditTime: 2020-07-30 15:03:26
@FilePath: /LeetCode/114.py
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: return None
        if root.left != None:
            left_tree = root.left
            # 找左子树的最右侧的节点
            node = left_tree
            while node.right != None:
                node = node.right
            right_tree = root.right

            node.right = right_tree
            root.right = left_tree
            root.left = None
        self.flatten(root.right)