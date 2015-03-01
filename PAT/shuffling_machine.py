#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    def __init__(self):
        pass
    def shuffling(self, times, order):
        porker = []
        result = []
        type = ['S', 'H', 'C', 'D']
        for i in type:
            for j in range(1, 14):
                porker.append(i + str(j))
        porker.append('J1')
        porker.append('J2')
        result = porker[:]
        for i in range(times):
            for j in range(len(order)):
                result[int(order[j]) - 1] = porker[j]
            porker = result[:]
        return " ".join(result)


if __name__ == "__main__":
    so = Solution()
    times = input()
    order = raw_input()
    order = order.split(" ")
    print so.shuffling(times, order)