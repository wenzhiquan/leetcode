package com.wen.maxDepthOfBinTree;


public class Solution {
	private TreeNode root;

	public Solution() {
		root = null;
	}

	private class TreeNode {

		int val;
		TreeNode left;
		TreeNode right;

		TreeNode(int x) {
			val = x;
		}

	}

	private void buildTree(TreeNode node, int data) {
		if (root == null)
			root = new TreeNode(data);
		else {
			if (node.left == null)
				node.left = new TreeNode(data);
			else if (node.right == null)
				node.right = new TreeNode(data);
			else {
				buildTree(node.left, data);
			}
		}

	}

	public int maxDepth(TreeNode node) {
		
		if(node == null) return 0;
		else{
			if(node.left == null || node.right == null)
				return maxDepth(node.left) + maxDepth(node.right) + 1;
			return Math.max(maxDepth(node.right), maxDepth(node.left)) + 1;
		}

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = { 5, 4, 8, 11, 13, 4, 7, 2, 1, 4};
		Solution so = new Solution();

		for (int i = 0; i < a.length; i++) {
			so.buildTree(so.root, a[i]);
		}

		System.out.println(so.maxDepth(so.root));
	}

}
