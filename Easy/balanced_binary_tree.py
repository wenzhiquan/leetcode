#!usr/bin/env python
# -*- coding:utf-8 -*-


# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean

    def __init__(self):
        self.root = None

    def isBalanced(self, root):
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        if root == None:
            return 0

        l = self.dfsHeight(root.left)
        if l == - 1:
            return -1
        r = self.dfsHeight(root.right)
        if r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1

    # def isBalanced(self, root):
    #     if root == None:
    #         return True
    #     else:
    #         l = self.maxDepth(root.left)
    #         n = self.maxDepth(root.right)
    #         if abs(l - n) < 2:
    #             return self.isBalanced(root.left) and self.isBalanced(root.right)
    #         else:
    #             return False

    # def maxDepth(self, root):
    #     if root == None:
    #         return 0
    #     else:
    #         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def buildTree(self, node, data):
        if self.root == None:
            self.root = TreeNode(data)
        else:
            if node.left == None:
                node.left = TreeNode(data)
            elif node.right == None:
                node.right = TreeNode(data)
            else:
                self.buildTree(node.left, data)

if __name__ == "__main__":
    so = Solution()
    a = [5, 4, 8, 11, 13, 4, 7, 2, 1, 4]
    for i in range(len(a)):
        so.buildTree(so.root, a[i])
    print(so.isBalanced(so.root))
