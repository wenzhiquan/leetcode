#!usr/bin/env python
# -*- coding:utf-8 -*-

# @author: wenzhiquan
# @author: 15/4/7
# @description:


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.root = None

    def minDepth(self, root):
        if not root:
            return 0
        else:
            if root.left is None:
                return self.minDepth(root.right) + 1
            elif root.right is None:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

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
    elements = '12'
    for i in elements:
        so.build_tree(so.root, i)
    print(so.minDepth(so.root))