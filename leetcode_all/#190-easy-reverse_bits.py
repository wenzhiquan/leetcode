#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if not n:
            return n
        else:
            bit = 1
            result = 0
            while bit < 2147483648:
                if bit & n:
                    result += 1
                bit <<= 1
                result <<= 1
            return result


if __name__ == "__main__":
    so = Solution()
    n = 43261596
    print(so.reverseBits(n))