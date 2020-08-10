'''
Date: 2020-08-06 17:58:05
LastEditors: FrankCast1e
LastEditTime: 2020-08-10 10:45:30
FilePath: /Leetcode/148.py
'''
from utils import ListNode, create_ListNode_from_list

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        head_list = []
        temp = head
        if head == None:
            return None
        while temp != None:
            head_list.append(temp)
            temp = temp.next
            head_list[-1].next = None
        piece_len = 1
        node_num = len(head_list)
        while piece_len < node_num:
            i = 0
            merged_head_list = []
            while i+1 < len(head_list):
                list_node1 = head_list[i]
                list_node2 = head_list[i+1]

                merge_head = self.merge_sorted_lists(list_node1, list_node2)
                merged_head_list.append(merge_head)
                i = i + 2
            if len(head_list) % 2 == 1:
                merged_head_list.append(head_list[-1])
            head_list = merged_head_list
            piece_len *= 2
        return head_list[0]

    def merge_sorted_lists(self, list_head1, list_head2):
        abstract_node = ListNode(0)
        temp = abstract_node
        while list_head1 != None and list_head2 != None:
            if list_head1.val < list_head2.val:
                temp.next = list_head1
                list_head1 = list_head1.next
                temp = temp.next
            else:
                temp.next = list_head2
                list_head2 = list_head2.next
                temp = temp.next
        if list_head1 != None:
            while list_head1 != None:
                temp.next = list_head1
                list_head1 = list_head1.next
                temp = temp.next
        if list_head2 != None:
            while list_head2 != None:
                temp.next = list_head2
                list_head2 = list_head2.next
                temp = temp.next
        return abstract_node.next


    

x = Solution()
node = create_ListNode_from_list([])
ans = x.sortList(node)
print("")