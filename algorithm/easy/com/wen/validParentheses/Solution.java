package com.wen.validParentheses;

import java.util.Stack;

public class Solution {

	public boolean isValid(String s) {

		Stack<Character> stack = new Stack<Character>();

		char[] tmp = s.toCharArray();

		for (int i = 0; i < tmp.length; i++) {
			if (tmp[i] == '(' || tmp[i] == '[' || tmp[i] == '{')
				stack.push(tmp[i]);
			else {
				if (stack.isEmpty()) return false;
				else{
					String decide = stack.pop() + "" + tmp[i];
					if (!decide.equals("()") && !decide.equals("{}")
							&& !decide.equals("[]"))
						return false;
				}
			}
		}

		if(stack.isEmpty()) return true;
		else return false;

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		System.out.println(so.isValid("]"));
	}

}
