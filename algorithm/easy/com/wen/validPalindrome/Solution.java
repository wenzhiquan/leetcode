package com.wen.validPalindrome;

public class Solution {
	
	public boolean isPalindrome(String s) {
		int i = 0;
		int j = s.length() - 1;
		
		while (i < j) {
			while(i < j && !Character.isLetterOrDigit(s.charAt(i))) i++;
			while(i < j && !Character.isLetterOrDigit(s.charAt(j))) j--;
			
			if(Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j)))
				return false;
			i++;
			j--;
		}
		
		return true;
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		System.out.println(so.isPalindrome("A man, a plan, a canal: Panama"));
	}

}
