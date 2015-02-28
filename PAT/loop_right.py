#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    def __init__(self):
        pass
    def loop_right(self, length, num, arr):
        seprate = length - num
        arr[0:seprate] = arr[seprate - 1::-1]
        arr[seprate:length] = arr[length - 1:seprate - 1:-1]
        arr = arr[::-1]
        return " ".join(arr)

if __name__ == "__main__":
    so = Solution()
    input = raw_input().split(" ")
    length = int(input[0])
    num = int(input[1])
    arr = raw_input().split(" ")
    print so.loop_right(length, num, arr)