package com.wen.addTwoNumbers;

public class Solution {

	class ListNode {
		int val;
		ListNode next;

		ListNode(int x) {
			val = x;
			next = null;
		}
	}

	private ListNode head;

	public void createList(ListNode node, int x) {
		if (head == null)
			head = new ListNode(x);
		else {
			if (node.next == null)
				node.next = new ListNode(x);
			else
				createList(node.next, x);
		}
	}

	public void printList(ListNode node) {
		if (node != null) {
			System.out.println(node.val);
			printList(node.next);
		}
	}

//	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
//
//		if (l1 == null) return l2;
//		if (l2 == null) return l1;
//
//		ListNode result = new ListNode(0);
//		ListNode prev = result;
//
//		int tmp;
//		int isIn = 0;
//
//		while (l1 != null && l2 != null) {
//			tmp = l1.val + l2.val + isIn;
//			if (tmp > 9) {
//				prev.next = new ListNode(tmp - 10);
//				isIn = 1;
//				prev = prev.next;
//				l1 = l1.next;
//				l2 = l2.next;
//			} else {
//				prev.next = new ListNode(tmp);
//				isIn = 0;
//				prev = prev.next;
//				l1 = l1.next;
//				l2 = l2.next;
//			}
//		}
//
//		while (l1 != null) {
//			if (isIn + l1.val == 10) {
//				prev.next = new ListNode(0);
//				isIn = 1;
//				prev = prev.next;
//				l1 = l1.next;
//			} else {
//				prev.next = new ListNode(l1.val + isIn);
//				isIn = 0;
//				prev = prev.next;
//				l1 = l1.next;
//			}
//		}
//
//		while (l2 != null) {
//			if (isIn + l2.val == 10) {
//				prev.next = new ListNode(0);
//				isIn = 1;
//				prev = prev.next;
//				l2 = l2.next;
//			} else {
//				prev.next = new ListNode(l2.val + isIn);
//				isIn = 0;
//				prev = prev.next;
//				l2 = l2.next;
//			}
//		}
//
//		if (isIn == 1)
//			prev.next = new ListNode(isIn);
//
//		return result.next;
//
//	}
	
	 public ListNode addTwoNumbers(ListNode c1, ListNode c2) {
	        ListNode sentinel = new ListNode(0);
	        ListNode d = sentinel;
	        int sum = 0;
	        while (c1 != null || c2 != null) {
	            sum /= 10;
	            if (c1 != null) {
	                sum += c1.val;
	                c1 = c1.next;
	            }
	            if (c2 != null) {
	                sum += c2.val;
	                c2 = c2.next;
	            }
	            d.next = new ListNode(sum % 10);
	            d = d.next;
	        }
	        if (sum / 10 == 1)
	            d.next = new ListNode(1);
	        return sentinel.next;
	    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = { 1, 8, 9 };
		int[] b = { 9, 8 ,2};

		Solution so1 = new Solution();
		Solution so2 = new Solution();

		for (int i = 0; i < a.length; i++)
			so1.createList(so1.head, a[i]);
		for (int i = 0; i < b.length; i++)
			so2.createList(so2.head, b[i]);

		so1.printList(so1.addTwoNumbers(so1.head, so2.head));

	}

}
