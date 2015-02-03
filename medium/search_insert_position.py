#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0
        low = 0
        high = len(A) - 1

        while low <= high:
            mid = (high + low) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return high + 1

if __name__ == "__main__":
    so = Solution()
    a = [1, 3, 5, 6]
    print so.searchInsert(a, 0)