#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param num, a list of integer
    # @return an integer

    def rob(self, num):
        if not num:
            return 0
        a = 0
        b = 0

        for i in range(len(num)):
            if i % 2 == 0:
                a = max(a + num[i], b)
            else:
                b = max(b + num[i], a)
        return max(a, b)


if __name__ == "__main__":
    so = Solution()
    num = [1, 1, 1, 1, 2, 3, 4, 3, 6, 5, 7, 9]
    print(so.rob(num))
