package com.wen.removeDupFromSortedArray2;

public class Solution {
	public int removeDuplicates(int[] A) {

		if (A.length < 2)
			return A.length;
		
		int len = 2, itor = 2;
	    while (itor < A.length) {
	        if (A[itor] != A[len-2]) 
	            A[len++] = A[itor];
	        itor++;
	    }
		
		for (int i = 0; i < A.length; i++) {
			System.out.println(A[i]);
		} 

		return len;
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		int[] a = {1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,5};
		System.out.println(so.removeDuplicates(a));
	}

}
