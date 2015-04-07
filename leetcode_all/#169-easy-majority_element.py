#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/3
# @description:

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        major = num[0]
        count = 0
        for i in num:
            if i == major:
                count += 1
            else:
                count -= 1
                if count < 0:
                    major = i
                    count = 0
        return major

if __name__ == "__main__":
    so = Solution()
    num = "12121234455111123424114444"
    print(so.majorityElement(num))