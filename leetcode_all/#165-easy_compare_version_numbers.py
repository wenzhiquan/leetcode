#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/3
# @description:


class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        arr1 = version1.split(".")
        arr2 = version2.split(".")
        length = max(len(arr2), len(arr1))
        for i in range(len(arr1)):
            arr1[i] = int(arr1[i])
        for i in range(len(arr2)):
            arr2[i] = int(arr2[i])
        for i in range(length - len(arr1)):
            arr1.append(0)
        for i in range(length - len(arr2)):
            arr2.append(0)
        for i in range(length):
            if arr1[i] > arr2[i]:
                return 1
            elif arr1[i] < arr2[i]:
                return -1
        return 0


if __name__ == "__main__":
    so = Solution()
    version1 = "01"
    version2 = "1.0.0.0"
    print(so.compareVersion(version1, version2))