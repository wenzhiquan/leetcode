package com.wen.removeNthNodeFromEndOfList;

public class Solution {
	private ListNode header;

	class ListNode {
		int val;
		ListNode next;

		ListNode(int x) {
			val = x;
			next = null;
		}
	}

	public Solution() {
		header = null;
	}

	public void buildList(ListNode node, int data) {
		if (header == null) {
			header = new ListNode(data);
		} else {
			if (node.next == null)
				node.next = new ListNode(data);
			else
				buildList(node.next, data);
		}
	}

	public void printList(ListNode node) {
		if (node != null) {
			System.out.println(node.val);
			printList(node.next);
		}
	}

	public ListNode removeNthFromEnd(ListNode head, int n) {
		
		if(head == null) return null;
		
		ListNode fast = head;
		ListNode slow = head;
		
		for(int i=0;i<n;i++) fast = fast.next;
		
		if(fast == null) return slow.next;
		
		while(fast.next != null){
			fast = fast.next;
			slow = slow.next;
		}
		
		slow.next = slow.next.next;
		
		return head;

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = { 1, 2, 3, 4, 5, 6, 7 };

		Solution so = new Solution();
		for (int i = 0; i < a.length; i++) {
			so.buildList(so.header, a[i]);
		}

		so.printList(so.removeNthFromEnd(so.header, 7));
	}

}
