#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return True
        else:
            result = ['[]', '{}', '()']
            parenthese = []
            for i in s:
                if i in '{([':
                    parenthese.append(i)
                else:
                    if len(parenthese) == 0:
                        return False
                    tmp = parenthese.pop() + i
                    if tmp not in result:
                        return False
            if not parenthese:
                return True
            else:
                return False

if __name__ == "__main__":
    so = Solution()
    s = '[[]]'
    print(so.isValid(s))