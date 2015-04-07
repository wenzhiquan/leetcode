#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/3
# @description:


class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

if __name__ == "__main__":
    so = Solution()
    print(so.trailingZeroes(25))
