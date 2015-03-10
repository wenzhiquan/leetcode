#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        bit = 1
        while bit <= 2147483648:
            result <<= 1
            if bit & n:
                result += 1
            bit <<= 1
        return result


if __name__ == "__main__":
    so = Solution()
    print so.reverseBits(43261596)
