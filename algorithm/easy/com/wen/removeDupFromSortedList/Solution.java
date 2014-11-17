package com.wen.removeDupFromSortedList;

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

	public ListNode deleteDuplicates(ListNode head) {

		if (head == null)
			return null;
		else if(head.next == null)
			return head;
		else {
			ListNode result = new ListNode(0);
			ListNode prev = result;

			while (head.next != null) {
				if (head.val == head.next.val) {
					head = head.next;
					if(head.next == null)
						prev.next = head;
				} else {
					prev.next = head;
					head = head.next;
					prev = prev.next;
				}
			}

			return result.next;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = { 1, 1 };

		Solution so = new Solution();
		for (int i = 0; i < a.length; i++) {
			so.buildList(so.header, a[i]);
		}

		so.printList(so.deleteDuplicates(so.header));
	}

}
