#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) < 1:
            return None
        max_length = 0
        start = 0

        for i in xrange(len(s)):
            if i - max_length > 1 and s[i - max_length - 1: i + 1] == s[i - max_length - 1: i + 1][:: -1]:
                start = i - max_length - 1
                max_length += 2
                continue

            if i - max_length > 0 and s[i - max_length: i + 1] == s[i - max_length: i + 1][:: -1]:
                start = i - max_length
                max_length += 1

        return s[start: start + max_length]

if __name__ == "__main__":
    so = Solution()
    print so.longestPalindrome("abcacbcddefxzxfeddcb")