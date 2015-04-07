#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/3
# @description:

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        else:
            result = [[1] for i in range(numRows)]
            for i in range(numRows):
                for j in range(1, i + 1):
                    if j == i:
                        result[i].append(1)
                        break
                    else:
                        result[i].append(result[i - 1][j - 1] + result[i - 1][j])
            return result
if __name__ == "__main__":
    so = Solution()
    rows = 10
    print(so.generate(rows))