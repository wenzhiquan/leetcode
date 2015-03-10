#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        needle_len = len(needle)
        haystack_len = len(haystack)
        if haystack_len < needle_len:
            return -1
        needle_index = needle_len - 1
        result = 0
        haystack_index = result + needle_index
        while haystack_index < haystack_len:
            while needle_index >= 0 and needle[needle_index] == haystack[haystack_index]:
                needle_index -= 1
                haystack_index -= 1
            if needle_index < 0:
                return result
            bad_move = self.find_index(needle, haystack[haystack_index])
            needle_index = bad_move
            result = haystack_index - needle_index
            needle_index = needle_len - 1
            haystack_index = result + needle_index
        return -1

    def find_index(self, s, c):
        return s.index(c) if c in s else -1
    def suffies(self, s, length):
        pass
    def good_suffix(self, s):
        pass

if __name__ == "__main__":
    so = Solution()
    print so.suffies('abaab', 5)
    print so.strStr('acabaabaabcacaabc', 'abaabc')
