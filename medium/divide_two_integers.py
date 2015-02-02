#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Administrator'


class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend == 0 or divisor == 0:
            return 0
        flag = 1
        MAX_INT = 2147483647
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            flag = -1
        dividend = dividend >= 0 and dividend or -dividend
        divisor = divisor >= 0 and divisor or -divisor
        result = 0
        cate, sub = 1, divisor
        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                result += cate
                sub <<= 1
                cate <<= 1
            else:
                sub >>= 1
                cate >>= 1
        result = flag == -1 and -result or result
        if result > MAX_INT:
            return MAX_INT
        else:
            return result

if __name__ == "__main__":
    so = Solution()
    print so.divide(24, 5)
