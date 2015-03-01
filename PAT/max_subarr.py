#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    def __init__(self):
        pass
    def max_sub(self, num, arr):
        max = 0
        sum = 0
        arr = arr.split(" ")
        for i in range(num):
            sum += int(arr[i])
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max

if __name__ == "__main__":
    so = Solution()
    num = input()
    arr = raw_input()
    print so.max_sub(num, arr)