#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @return an integer
    def reverse(self, x):
        s = list(str(x))
        symbol = 1
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if s[0] == '-':
            symbol = 0
            del s[0]
        s.reverse()
        print(s)
        if symbol == 0:
            s.insert(0, '-')
        s = "".join(s)
        result = int(s)
        if result > MAX_INT or result < MIN_INT:
            result = 0
        return result

if __name__ == "__main__":
    so = Solution()
    x = -1000000003
    print(so.reverse(x))
