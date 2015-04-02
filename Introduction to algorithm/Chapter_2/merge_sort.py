#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/3/24
# @description:


class Solution(object):
    def merge_sort(self, arr, left, right):
        if left < right:
            div = (left + right) // 2
            self.merge_sort(arr, left, div)
            self.merge_sort(arr, div + 1, right)
            self.merge(arr, left, div, right)
            return arr


    def merge(self, arr, left, div, right):
        larr = rarr = []
        larr = arr[left: div + 1]
        llength = len(larr)
        rarr = arr[div + 1: right + 1]
        rlength = len(rarr)
        i = j = 0
        k = left
        while True:
            if larr[i] < rarr[j]:
                arr[k] = larr[i]
                i += 1
            else:
                arr[k] = rarr[j]
                j += 1
            k += 1
            if i >= llength or j >= rlength:
                break
        while i < llength:
            arr[k] = larr[i]
            i += 1
            k += 1
        while j < rlength:
            arr[k] = rarr[j]
            j += 1
            k += 1

if __name__ == "__main__":
    so = Solution()
    arr = [5, 2, 4, 7, 1, 3, 2, 6, 8, 9, 1, 10]
    print(so.merge_sort(arr, 0, len(arr) - 1))
