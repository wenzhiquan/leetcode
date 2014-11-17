package com.wen.mergeSortedArray;


public class Solution {
	
	public int[] merge(int A[], int m, int B[], int n) {
		
			int i = m - 1;
			int j = n - 1;
			int k = m + n - 1;
			
			while(i >= 0 && j >= 0){
				if(A[i] > B[j])
					A[k--] = A[i--];
				else
					A[k--] = B[j--];
			}
			while(j >= 0){
				A[k--] = B[j--];
			}
		
	        return A;
	    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		int a[] = {1,3,5,7,9,0,0,0,0};
		int b[] = {2,6,6,10};
		int out[] = so.merge(a, 5, b, 4);
		for(int i = 0;i<out.length;i++){
			System.out.println(out[i]);
		}
		
	}

}
