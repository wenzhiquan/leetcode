package com.wen.singleNumber2;

public class Solution {

	public int singleNumber(int[] A) {
		int ones = 0, twos = 0;

		for (int i = 0; i < A.length; i++) {
			ones = (ones ^ A[i]) & ~twos;
			twos = (twos ^ A[i]) & ~ones;
		}
		return ones;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = { 1, 1, 1, 8, 2, 4, 3, 5, 6, 7, 2, 3, 2, 3, 4, 5, 5, 6, 6, 7,
				7, 4, 12, 12, 12 };
		Solution so = new Solution();
		System.out.println(so.singleNumber(a));
	}
}
