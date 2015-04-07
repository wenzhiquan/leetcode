#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/3
# @description:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def __init__(self):
        self.header = None

    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        else:
            temp_a = headA
            temp_b = headB
            result = ListNode(0)
            prev = result
            while temp_a is not None and temp_b is not None:
                if temp_a.val == temp_b.val:
                    prev.next = temp_a
                    temp_a = temp_a.next
                    temp_b = temp_b.next
                    prev = prev.next
                else:
                    if temp_a.next is None and temp_b.next is None:
                        if temp_a.val != temp_b.val:
                            return None
                    temp_a = temp_a.next
                    temp_b = temp_b.next
                    if temp_b is None:
                        temp_b = headA
                    elif temp_a is None:
                        temp_a = headB
            return result.next

    def bulid_list(self, node, data):
        if self.header is None:
            self.header = ListNode(data)
        else:
            if node.next is None:
                node.next = ListNode(data)
            else:
                self.bulid_list(node.next, data)

if __name__ == "__main__":
    so = Solution()
    so2 = Solution()
    list1 = "345789"
    list2 = "67789"
    for i in list1:
        so.bulid_list(so.header, i)
    for i in list2:
        so2.bulid_list(so2.header, i)
    result = so.getIntersectionNode(so.header, so2.header)
    while result is not None:
        print(result.val)
        result = result.next
