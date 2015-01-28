#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        hashtable = {}
        max_length, start = 0, 0


        for index, value in enumerate(s):
            if value in hashtable:
                start = max(hashtable[value] + 1, start)
            hashtable[value] = index
            max_length = max(max_length, index - start + 1)

        return max_length



if __name__ == "__main__":
    so = Solution()
    print so.lengthOfLongestSubstring("abcabcddefxz")