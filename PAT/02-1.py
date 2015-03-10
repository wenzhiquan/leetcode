#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'
from sys import stdout


class Solution:
    def calculate(self, num):
        flag = 0
        for i in xrange(0, len(num), 2):
            if i == len(num) - 2 or i + 2 > len(num):
                break
            para = int(num[i])
            index = int(num[i + 1])
            para *= index
            if para:
                if flag:
                    stdout.write(" ")
                else:
                    flag = 1
                stdout.write(str(para) + " " + str(index - 1))
        if not flag:
            stdout.write('0 0')

if __name__ == "__main__":
    so = Solution()
    num = raw_input()
    num = num.split(" ")
    so.calculate(num)
