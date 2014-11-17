package com.wen.removeDupFromSortedArray;

public class Solution {

    public int removeDuplicates(int[] A) {
    	
    	if(A.length <= 1){
    		return A.length;
    	}
    	
    	int count = 0;
    	
    	for(int i=1;i<A.length;i++){
    		if(A[i] == A[i-1]) count++;
    		else A[i - count] = A[i];
    	}
    	
		return A.length - count;
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		int[] a = {1, 1, 1, 4, 4, 5, 8, 8, 8, 9};
		System.out.println(so.removeDuplicates(a));
	}

}
