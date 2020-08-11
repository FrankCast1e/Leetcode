'''
Date: 2020-08-10 10:43:58
LastEditors: FrankCast1e
LastEditTime: 2020-08-11 19:13:28
FilePath: /Leetcode/utils.py
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create_ListNode_from_list(num_list):
    if num_list == []:
        return None
    head = ListNode(num_list[0])
    temp = head
    i = 1
    while i < len(num_list):
        node = ListNode(num_list[i])
        temp.next = node
        temp = temp.next
        i += 1
    return head

def create_BinaryTree_from_list(num_list):
    root = TreeNode(num_list[0])
    node_list = list()
    node_list.append(root)
    depth = 1
    node_num = depth * 2
    base, offset = 1, 0
    while base+offset < len(num_list):
        if num_list[base+offset] == 'null':
            node_list.append(None)
        else:
            node = TreeNode(num_list[base+offset])
            # calculate father pos
            father_base = 0
            for i in range(depth-1):
                father_base += 2**i
            father_offset = offset // 2
            if (offset % 2) == 0:
                node_list[father_base+father_offset].left = node
            else:
                node_list[father_base+father_offset].right = node
            node_list.append(node)
        offset += 1
        if offset == node_num:
            base = base + offset
            depth += 1
            node_num = depth*2
            offset = 0
    return root