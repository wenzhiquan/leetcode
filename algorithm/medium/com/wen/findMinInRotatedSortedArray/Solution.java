package com.wen.findMinInRotatedSortedArray;

public class Solution {
    public int findMin(int[] num) {
    	int start = 0;
    	int end = num.length - 1;
    	int mid;
    	
    	while(start<end){
    		if(num[start] < num[end])
    			return num[start];
    		mid = (start + end)/2;
    		
    		if(num[start] <= num[mid])
    			start = mid + 1;
    		else end = mid;
    	}
    	
    	
		return num[start];
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = {4,5,6,7,8,1,2};
		
		Solution so = new Solution();
		System.out.println(so.findMin(a));
	}

}
