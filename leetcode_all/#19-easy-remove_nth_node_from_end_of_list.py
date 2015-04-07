#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def __init__(self):
        self.header = None

    def removeNthFromEnd(self, head, n):
        if not n:
            return head
        else:
            fast = head
            slow = head
            for i in range(n):
                fast = fast.next
            if fast is None:
                return slow.next
            while fast.next is not None:
                fast = fast.next
                slow = slow.next
            tmp = slow.next
            slow.next = tmp.next
            return head

    def bulit_list(self, node, data):
        if self.header is None:
            self.header = ListNode(data)
        else:
            if node.next is None:
                node.next = ListNode(data)
            else:
                self.bulit_list(node.next, data)

if __name__ == "__main__":
    so = Solution()
    list = "12345"
    for i in list:
        so.bulit_list(so.header, i)
    result = so.removeNthFromEnd(so.header, 0)
    while result is not None:
        print(result.val)
        result = result.next