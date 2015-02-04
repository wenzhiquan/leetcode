#!/bin/env python
#-*- encoding: UTF-8 -*-

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        #length = len(A)
        #begin = length - 1
        #for i in reversed(xrange(length - 1)):
        #    if i + A[i] >= begin:
        #        begin = i
        #return not begin
        jump = 1
        if len(A) == 1:
            return True
        for i in xrange(len(A) - 1):
            jump -= 1
            if A[i] > jump:
                jump = A[i]
            if jump == 0:
                return False
        return True

if __name__ == "__main__":
    so = Solution()
    print so.canJump([2, 0, 0])
