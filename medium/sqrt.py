#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Administrator'

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x <= 0:
            return 0
        low = 1
        high = x
        while low <= high:
            mid = (high + low) // 2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return mid
        return high

if __name__ == "__main__":
    so = Solution()
    print so.sqrt(17)