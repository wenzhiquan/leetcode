#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 1:
            return num[0]
        low = 0
        high = len(num) - 1
        if num[low] < num[high]:
            return num[0]
        while low != high - 1:
            mid = (high + low) // 2
            if num[mid] > num[high]:
                low = mid
            elif num[low] > num[mid]:
                high = mid
        return num[high]

if __name__ == "__main__":
    so = Solution()
    num = [1, 3, 0]
    print so.findMin(num)