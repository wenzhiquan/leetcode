#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        string = s.strip().split(" ")
        length = len(string) - 1
        while length >= 0:
            result = 0
            for i in string[length]:
                if not i.isalpha():
                    length -= 1
                    break
                result += 1
            if result == len(string[length]):
                return result
        return 0

if __name__ == "__main__":
    so = Solution()
    s = "H!ello World@"
    print(so.lengthOfLastWord(s))