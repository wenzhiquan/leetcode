#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def __init__(self):
        self.root = None

    def hasPathSum(self, root, sum):
        if root is None:
            return False
        else:
            if root.left is None and root.right is None and root.val - sum == 0:
                return True
            else:
                return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def build_tree(self, node, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            if node.left is None:
                node.left = TreeNode(data)
            elif node.right is None:
                node.right = TreeNode(data)
            else:
                self.build_tree(node.left, data)

if __name__ == "__main__":
    so = Solution()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in a:
        so.build_tree(so.root, i)
    print(so.hasPathSum(so.root, 14))