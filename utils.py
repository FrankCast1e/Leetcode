'''
Date: 2020-08-10 10:43:58
LastEditors: FrankCast1e
LastEditTime: 2020-08-10 10:45:03
FilePath: /Leetcode/utils.py
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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