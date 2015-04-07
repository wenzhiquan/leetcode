#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        string = list(str(x))
        if not string:
            return False
        else:
            length = len(string)
            for i in range(length // 2):
                if string[i] != string[length - 1 - i]:
                    return False
            return True


if __name__ == "__main__":
    so = Solution()
    x = 1234554321
    print(so.isPalindrome(x))