#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        row_num, col_num = len(matrix), len(matrix[0])
        low, high = 0, row_num * col_num - 1
        while low <= high:
            mid = (high + low) / 2
            mid_value = matrix[mid / col_num][mid % col_num]
            print mid
            if mid_value == target:
                return True
            elif mid_value > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
        # for i in xrange(len(matrix)):
        #     row = matrix[i]
        #     if len(row) == 0:
        #         return False
        #     if target > row[len(row) - 1]:
        #         continue
        #     low = 0
        #     high = len(row) - 1
        #     while low <= high:
        #         mid = (high + low) / 2
        #         if row[mid] > target:
        #             high = mid - 1
        #         elif row[mid] < target:
        #             low = mid + 1
        #         else:
        #             return True
        # return False

if __name__ == "__main__":
    so = Solution()
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print so.searchMatrix(matrix, 23)