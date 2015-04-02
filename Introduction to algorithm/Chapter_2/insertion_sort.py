#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/3/20
# @description:


class Solution:
    def insertion_sort_asc(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def insertion_sort_desc(self, arr):
        for i in range(len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

if __name__ == "__main__":
    so = Solution()
    arr = [5, 2, 4, 6, 1, 3]
    print(so.insertion_sort_desc(arr))