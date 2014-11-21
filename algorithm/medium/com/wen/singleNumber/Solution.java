package com.wen.singleNumber;

public class Solution {
	
    public int singleNumber(int[] A) {
        int result = 0;
        
        for(int i=0;i<A.length;i++)
        	result ^= A[i];
        return result;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = {1,1,2,3,2,3,4,5,5,6,6,7,7,4,12};
		Solution so = new Solution();
		System.out.println(so.singleNumber(a));
	}

}
