#!bin/env python
#-*- encoding:UTF-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        a = [roman_dict.get(v) for v in s]
        result = list(a)
        for i in xrange(len(a) - 1):
            if a[i] < a[i + 1]:
                result[i] = -a[i]
            else:
                result[i] = a[i]
        return sum(result)

if __name__ == "__main__":
    so = Solution()
    print so.romanToInt('CMXCIX')
