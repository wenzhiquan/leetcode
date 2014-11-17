package com.wen.removeElement;

public class Solution {
	
    public int removeElement(int[] A, int elem) {    	
    	int begin = 0;
    	for(int i=0;i<A.length;i++) if(elem != A[i]) A[begin++] = A[i];
    	for(int i=0;i<A.length;i++) System.out.println(A[i]);
		return begin;        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		int[] a = {1,1,2,3,2,1,4,5,6};
		so.removeElement(a, 1);
//		System.out.println(so.removeElement(a, 1));
	}

}
