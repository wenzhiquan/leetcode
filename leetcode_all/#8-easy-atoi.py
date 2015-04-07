#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @return an integer
    def atoi(self, str):
        string = list(str.strip())
        if not string:
            return 0
        symbol = ""
        result = ""
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if string[0] in '+-':
            symbol = string[0]
            del string[0]
        for i in string:
            if '0' <= i <= '9':
                result += i
            else:
                break
        if result:
            result = -int(result) if symbol == '-' else int(result)
            if result > MAX_INT:
                return MAX_INT
            if result < MIN_INT:
                return MIN_INT
        else:
            result = 0
        return result

if __name__ == "__main__":
    so = Solution()
    string = " -2147483649  "
    print(so.atoi(string))