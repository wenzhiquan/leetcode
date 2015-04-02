#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        length = len(num)
        if length < 3:
            return []
        two_sum = []
        three_sum = []
        for i in range(length):
            for j in range(i + 1, length):
                sum = num[i] + num[j]
                number = (num[i], num[j])
                dic = {sum: number}
                if dic not in two_sum and sum not in two_sum:
                    two_sum.append(sum)
        return three_sum

if __name__ == "__main__":
    so = Solution()
    num = [-1, 0, 1, 2, -1, -4]
    print(so.threeSum(num))
