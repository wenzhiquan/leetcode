#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    def __init__(self):
        pass
    def settler(self, num):
        num2 = num * 2
        tmp = num2
        num = sorted(str(num))
        num2 = sorted(str(num2))
        if num == num2:
            print "Yes"
        else:
            print "No"
        return tmp

if __name__ == "__main__":
    so = Solution()
    num = input()
    print so.settler(num)