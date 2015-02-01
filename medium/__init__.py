#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        low = 1
        high = x
        mark = 1
        while low != high - 1:
            mid = (high + low) / 2
            if mid * mid > x:
                high = mid
            elif mid * mid < x:
                mark = mid
                low = mid
            else:
                return mid
        return mark
        #ans = 0
        #bit = 1l << 15
        #while bit > 0:
        #    ans |= bit
        #    if ans * ans > x:
        #        ans ^= bit
        #    bit >>= 1
        #return int(ans)

if __name__ == "__main__":
    so = Solution()
    #print so.sqrt(3)
    for i in xrange(37):
        print so.sqrt(i)
