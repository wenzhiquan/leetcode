#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Administrator'


class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0 or x == 1:
            return 1
        result = 1.0
        if n < 0:
            x = result / x
            n = -n
        return (n % 2 == 0) and self.pow(x * x, n / 2) or x * self.pow(x * x, n / 2)

if __name__ == "__main__":
    so = Solution()
    print so.pow(2, -5)
