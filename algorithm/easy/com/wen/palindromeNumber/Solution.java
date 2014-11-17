package com.wen.palindromeNumber;

public class Solution {
	
	
	public boolean isPalindrome(int x) {
		
		if(x < 0)
			return false;
		else
			return x==reverse(x);
	}
		
	private int reverse(int x) {
		// TODO Auto-generated method stub
		int y = 0;
		
		while(x > 0){
			y = y * 10 + x % 10;
			x /= 10;
		}
		
		return y;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		System.out.println(so.isPalindrome(321343123));
	}

}
