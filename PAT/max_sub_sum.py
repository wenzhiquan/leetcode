#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    def __init__(self):
        pass
    def max_sub(self, num, arr):
        max = 0
        tmp_sum = 0
        start = 0
        end = num - 1
        tmp_start = 0
        tmp_end = 0
        arr = arr.split(" ")
        for i in range(num):
            if tmp_sum >= 0:
                tmp_sum += int(arr[i])
                tmp_end = i
            else:
                tmp_sum = int(arr[i])
                tmp_start = i
                tmp_end = i

            if tmp_sum > max or (tmp_sum == 0 and end == num - 1):
                max = tmp_sum
                start = tmp_start
                end = tmp_end
        print str(max) + " " + str(arr[start]) + " " + str(arr[end])

if __name__ == "__main__":
    so = Solution()
    num = input()
    arr = raw_input()
    so.max_sub(num, arr)