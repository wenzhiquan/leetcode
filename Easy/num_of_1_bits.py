#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param n, an integer
    # @return an integer
    def hammeringWeight(self, n):
        result = 0
        bit = 1
        while bit <= 2147483648:
            if bit & n:
                result += 1
            bit <<= 1
        return result


if __name__ == "__main__":
    so = Solution()
    print so.hammeringWeight(43261596)
