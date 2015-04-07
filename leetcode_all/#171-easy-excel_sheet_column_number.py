#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/3
# @description:


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result = 0
        l = len(s)
        for i in s:
            l -= 1
            result += (ord(i) - 64) * 26 ** l
        return result

if __name__ == "__main__":
    so = Solution()
    print(so.titleToNumber("BAA"))
