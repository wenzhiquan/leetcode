package com.wen.pathSum;


public class Solution {
	
	private TreeNode root;
	
	public Solution(){
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
	
	private void buildTree(TreeNode node, int data){
		if(root == null)
			root = new TreeNode(data);
		else{
			if(node.left == null)
				node.left = new TreeNode(data);
			else if(node.right == null)
				node.right = new TreeNode(data);
			else{
				buildTree(node.left, data);
			}
		}
		
	}
	
	 public void preOrder(TreeNode node){  
	        if(node != null){  
	            System.out.println(node.val);  
	            preOrder(node.left);  
	            preOrder(node.right);  
	        }  
	    }  

	public boolean hasPathSum(TreeNode node, int sum) {
		if(node == null) return false;
		
		if(node.left == null && node.right == null && sum - node.val == 0) return true;
		
		return hasPathSum(node.left, sum - node.val) || hasPathSum(node.right, sum - node.val);

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = {5,4,8,11,13,4,7,2,1};
		Solution so = new Solution();
		
		for(int i=0;i<a.length;i++){
			so.buildTree(so.root, a[i]);
		}
		so.preOrder(so.root); 
		
		System.out.println(so.hasPathSum(so.root, 22));
	}

}
