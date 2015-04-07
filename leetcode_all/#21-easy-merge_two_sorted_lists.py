#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/2
# @description:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def __init__(self):
        self.header = None

    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result = ListNode(0)
        temp = result
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1 is not None:
            temp.next = l1
        if l2 is not None:
            temp.next = l2
        return result.next

    def buildList(self, node, data):
        if self.header is None:
            self.header = ListNode(data)
        else:
            if node.next is None:
                node.next = ListNode(data)
            else:
                self.buildList(node.next, data)

if __name__ == "__main__":
    so = Solution()
    so2 = Solution()
    l1 = "223489"
    l2 = "145678"
    for i in l1:
        so.buildList(so.header, i)
    for i in l2:
        so2.buildList(so2.header, i)
    result = so.mergeTwoLists(so.header, so2.header)
    while result is not None:
        print(result.val)
        result = result.next