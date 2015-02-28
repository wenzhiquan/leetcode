#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    def __init__(self):
        pass

    def prime_pair(self, num):
        if num < 4:
            return 0
        prime_arr = [2]
        pair = 0
        for i in range(3, num + 1):
            if self.is_prime(i):
                prime_arr.append(i)
        for i in xrange(1, len(prime_arr)):
            if prime_arr[i] - prime_arr[i - 1] == 2:
                pair += 1
        return pair

    def is_prime(self, num):
        for i in xrange(2, num):
            if num % i == 0:
                return False
            if i * i > num:
                break
        return True

if __name__ == "__main__":
    so = Solution()
    num = input()
    print so.prime_pair(num)