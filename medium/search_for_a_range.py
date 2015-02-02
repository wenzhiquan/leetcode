#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Administrator'


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = self.binary_search(A, target - 0.5)
        if A[left] != target:
            return [-1, -1]
        A.append(0)
        right = self.binary_search(A, target + 0.5)
        return [left, right - 1]

    def binary_search(self, A, target):
        low = 0
        high = len(A) - 1

        while low < high:
            mid = (high + low) / 2
            if A[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

if __name__ == "__main__":
    so = Solution()
    print so.searchRange([1, 1], 3)
