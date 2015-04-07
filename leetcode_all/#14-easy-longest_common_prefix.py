#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        else:
            prefix = strs[0]
            length = len(prefix)
            for i in strs:
                while i[:length] != prefix:
                    length -= 1
                    prefix = prefix[:length]
            return prefix

if __name__ == "__main__":
    so = Solution()
    strs = ['asdf', 'adfe', 'asdfww', 'asdffd']
    print(so.longestCommonPrefix(strs))