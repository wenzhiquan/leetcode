package com.wen.binTreeLevelOrderTraversal2;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

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

    public List<List<Integer>> levelOrder(TreeNode root) {
    	if(root == null) return new ArrayList<List<Integer>>();
    	
    	List<List<Integer>> result = new ArrayList<List<Integer>>();
    	LinkedList<TreeNode> nodeList = new LinkedList<TreeNode>();
    	List<Integer> tmp = new ArrayList<Integer>();
    	
    	TreeNode lastNode = root;
    	
    	nodeList.add(root);
    	
    	while(nodeList.size() > 0){
    		TreeNode currentNode = nodeList.poll();
    		tmp.add(currentNode.val);
    		if(currentNode.left != null) nodeList.add(currentNode.left);
    		if(currentNode.right != null) nodeList.add(currentNode.right);
    		
    		if(currentNode == lastNode){
    			result.add(0, tmp);
    			tmp = new ArrayList<Integer>();
    			lastNode = nodeList.peekLast();
    		}
    	}
    	
		return result;
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = { 5, 4, 8, 11, 13, 4, 7, 2, 1, 4};
		Solution so = new Solution();

		for (int i = 0; i < a.length; i++) {
			so.buildTree(so.root, a[i]);
		}

		System.out.println(so.levelOrder(so.root));
	}

}
