#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/3
# @description:


class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows < 2 or len(s) < 2:
            return s
        else:
            result = [""] * nRows
            print(result)
            for i in range(len(s)):
                row = i % (2 * nRows - 2)
                print(row)
                if row >= nRows:
                    result[nRows - row - 2] += s[i]
                else:
                    result[row] += s[i]
            return "".join(result)

if __name__ == "__main__":
    so = Solution()
    s = "PAYPALISHIRING"
    rows = 5
    print(so.convert(s, rows))