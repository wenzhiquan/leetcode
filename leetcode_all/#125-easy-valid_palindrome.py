#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        string = s.strip()
        if not string:
            return True
        else:
            char_list = []
            for i in string:
                if i.isalnum():
                    char_list.append(i.lower())
            length = len(char_list)
            for i in range(length // 2):
                if char_list[i] != char_list[length - 1 - i]:
                    return False
            return True

if __name__ == "__main__":
    so = Solution()
    s = '`l;`` 1o1 ??;l`'
    print(so.isPalindrome(s))