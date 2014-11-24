package com.wen.climbingStairs;

public class Solution {
	
    public int climbStairs(int n) {
    	
    	if(n<2) return 1;
    	
    	int[] tmp = new int[n];
    	tmp[0] = 1;
    	tmp[1] = 2;
    	
    	for(int i=2;i<n;i++) tmp[i] = tmp[i-1] + tmp[i-2];
    	
		return tmp[n-1];
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		System.out.println(so.climbStairs(100));
	}

}
