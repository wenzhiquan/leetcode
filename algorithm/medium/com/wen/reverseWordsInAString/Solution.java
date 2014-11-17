package com.wen.reverseWordsInAString;

public class Solution {

	public String reverseWords(String s) {

		if (s.isEmpty())
			return "";
		else {
			if (s.contains(" ")) {
				String[] tmp = s.split(" ");
				String exchange;
				String result = "";
				for (int i = 0; i < tmp.length/2; i++) {
					exchange = tmp[i];
					tmp[i] = tmp[tmp.length - 1 - i];
					tmp[tmp.length - 1 - i] = exchange;
				}
				
				for (int i = 0; i < tmp.length; i++) {
					if(!tmp[i].equals(""))
						result += " " + tmp[i];
				}
				
				return result.trim();
			} else
				return s;
		}

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		System.out.println(so.reverseWords("  a  b "));
	}

}
