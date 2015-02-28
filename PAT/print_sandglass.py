#!/bin/env python
#-*- encoding:utf-8 -*-#

class Solution:
    def __init__(self):
        pass
    def print_sandglass(self, input):
        input = input.split(" ")
        num = int(input[0])
        symbol = input[1]
        tmp = 0
        left = 0
        
        if num == 1:
            print num * symbol
        for i in range(1, num, 2):
            tmp += 2 * i
            if tmp - 1 > num:
                left = num - (tmp - 1 - 2 * i)
                tmp = i - 2
                break

        for i in range(tmp):
            if i <= tmp / 2:
                print i * " " + (tmp - 2 * i) * symbol
            else:
                print (tmp - i - 1) * " " + (2 * (i + 1) - tmp) * symbol

        print left


if __name__ == "__main__":
    so = Solution()
    input = raw_input()
    so.print_sandglass(input)
