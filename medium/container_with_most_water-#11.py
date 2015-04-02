#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @return an integer
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = (right - left) * (min(height[left], height[right]))
        while left < right:
            if height[left] > height[right]:
                right -= 1
                if height[right] > height[right + 1]:
                    max_area = max(max_area, (right - left) * min(height[left], height[right]))
            else:
                left += 1
                if height[left] > height[left - 1]:
                    max_area = max(max_area, (right - left) * min(height[left], height[right]))
        return max_area

if __name__ == "__main__":
    so = Solution()
    height = [4, 3, 3, 2, 3, 1, 2, 4]
    print(so.maxArea(height))