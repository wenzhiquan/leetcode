#!/bin/env python
#-*- encoding: UTF-8 -*-

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        #start = len(gas) - 1
        #end = 0
        #sum = gas[start] - cost[start]
        #while start > end:
        #    if sum >= 0:
        #        sum += gas[end] - cost[end]
        #        end += 1
        #    else:
        #        start -= 1
        #        sum += gas[start] - cost[start]
        #if sum >= 0:
        #    return start
        #else:
        #    return -1
        total_gas, total_cost = 0, 0
        max_diff, diff = 2147483648, 0
        station = 0
        for i in xrange(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            diff = total_gas - total_cost
            if diff < max_diff:
                max_diff = diff
                station = i
        if total_cost > total_gas:
            return -1
        station += 1
        if station == len(gas):
            station = 0
        return station

if __name__ == "__main__":
    so = Solution()
    print so.canCompleteCircuit([3, 1, 2], [1, 3, 2])
