#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        tmp = [roman_dict.get(i) for i in s]
        length = len(tmp) - 1
        for i in range(length):
            if tmp[i] < tmp[i + 1]:
                result -= tmp[i]
            else:
                result += tmp[i]
        result += tmp[length]
        return result

if __name__ == "__main__":
    so = Solution()
    s = 'MCM'
    print(so.romanToInt(s))