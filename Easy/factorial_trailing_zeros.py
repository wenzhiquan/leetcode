#!bin/env python
#-*- encoding:UTF-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            n /= 5
            result += n
        return result

if __name__ == "__main__":
    so = Solution()
    print so.trailingZeroes(30)
