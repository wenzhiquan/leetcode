#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @return a string
    def convert(self, s, nRows):
        if len(s) < 3 or nRows <= 1:
            return s
        result, tmp = "", [""] * nRows
        for i in xrange(len(s)):
            index = i % (2 * nRows - 2)
            if index < nRows:
                tmp[index] += s[i]
            else:
                tmp[2 * nRows - index - 2] += s[i]
        for i in tmp:
            result += i
        return result

if __name__ == "__main__":
    so = Solution()
    print so.convert("PAYPALISHIRING", 3)