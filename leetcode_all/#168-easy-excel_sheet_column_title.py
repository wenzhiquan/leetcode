#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/3
# @description:


class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = []
        while num > 0:
            temp = num % 26
            if temp == 0:
                temp = 26
            result.insert(0, chr(temp + 64))
            num -= temp
            num //= 26
        return "".join(result)

if __name__ == "__main__":
    so = Solution()
    print(so.convertToTitle(53))