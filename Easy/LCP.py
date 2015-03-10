#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        length = len(prefix)
        for i in xrange(1, len(strs)):
            length = min(length, len(strs[i]))
            while length and prefix[:length] != strs[i][:length]:
                length -= 1
        return "" if not length else prefix[:length]



if __name__ == "__main__":
    so = Solution()
    strs = ['asd', 'asde', 'as', 'asrd', 'a']
    print so.longestCommonPrefix(strs)
