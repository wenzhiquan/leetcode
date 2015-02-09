#!bin/env python
#-*- encoding:UTF-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        while n > 1:
            count = 1
            temp = ''
            for i in xrange(1, len(s)):
                if s[i] != s[i - 1]:
                    temp += str(count)
                    temp += s[i - 1]
                    count = 1
                else:
                    count += 1
            temp += str(count)
            temp += s[-1]
            s = temp
            n -= 1
        return s

if __name__ == "__main__":
    so = Solution()
    print so.countAndSay(5)
