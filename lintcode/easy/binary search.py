#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Administrator'

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] > target - 0.5:
                high = mid - 1
            elif nums[mid] < target - 0.5:
                low = mid + 1
        if nums[high + 1] == target:
            return high + 1
        else:
            return -1

if __name__ == "__main__":
    so = Solution()
    print so.binarySearch([1, 2, 3, 3, 4, 4, 4, 5, 10], 1)