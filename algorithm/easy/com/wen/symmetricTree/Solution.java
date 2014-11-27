package com.wen.symmetricTree;

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

    public boolean isSymmetric(TreeNode root) {
    	if(root == null) return true;
    	
		return check(root.left, root.right);
        
    }
    
    public boolean check(TreeNode lTree, TreeNode rTree){
    	if(lTree == null && rTree == null) return true;
    	else if(lTree == null) return false;
    	else if(rTree == null) return false;
    	
    	if(lTree.val != rTree.val) return false;
    	else return check(rTree.left, lTree.right) && check(lTree.left, rTree.right);
    }
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = { 5, 4, 8, 11, 13, 4, 7, 2, 1, 4};
		Solution so = new Solution();

		for (int i = 0; i < a.length; i++) {
			so.buildTree(so.root, a[i]);
		}

		System.out.println(so.isSymmetric(so.root));
	}

}
