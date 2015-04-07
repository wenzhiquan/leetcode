#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.min = 0
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    # @return nothing
    def pop(self):
        tail = len(self.stack) - 1
        element = self.stack[tail]
        if element < 0:
            self.min -= element
        del self.stack[tail]

    # @return an integer
    def top(self):
        tail = len(self.stack) - 1
        element = self.stack[tail]
        if tail == 0:
            return element
        if element < 0:
            return self.min
        else:
            return self.min + element

    # @return an integer
    def getMin(self):
       return self.min

if __name__ == "__main__":
    so = MinStack()
    so.push(1)
    so.push(2)
    # so.push(-1)
    # so.push(3)
    # so.push(6)
    print(so.top())
    print(so.getMin())
    so.pop()
    # so.pop()
    # print(so.top())
    # so.pop()
    print(so.getMin())
    print(so.top())