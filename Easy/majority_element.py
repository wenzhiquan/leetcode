#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        # hashed = {}
        # most = len(num) // 2
        # for index, value in enumerate(num):
        #     if value in hashed:
        #         hashed[value] += 1
        #     else:
        #         hashed[value] = 1
        #     if hashed[value] >= most:
        #             return value
        counter = 0
        candidate = num[0]
        for i in xrange(len(num)):
            if num[i] == candidate:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    candidate = num[i]
                    counter = 1
        return candidate

if __name__ == "__main__":
    so = Solution()
    a = [6, 5, 5]
    print so.majorityElement(a)