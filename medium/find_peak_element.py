#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) <= 1:
            return 0
        low = 0
        high = len(num) - 1
        while low <= high:
            mid = (high + low) / 2

            if mid == 0 and num[mid] > num[mid + 1]:
                return mid
            elif mid == len(num) - 1 and num[mid] > num[mid - 1]:
                return mid
            if num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
                return mid
            elif num[mid] < num[mid - 1]:
                high = mid - 1
            elif num[mid] < num[mid + 1]:
                low = mid + 1
        return mid + 1


if __name__ == "__main__":
    so = Solution()
    a = [1, 3, 2, 4, 1, 2, 1, 2, 1, 3]
    print so.findPeakElement(a)