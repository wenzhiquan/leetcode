package com.wen.mergeTwoSortedList;

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

	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
		
		if(l1 == null && l2 == null)
			return null;
		else if(l1 == null)
			return l2;
		else if(l2 == null)
			return l1;
		else{
			
			ListNode result = new ListNode(0);
	        ListNode prev = result;
			
	        while(l1 != null && l2 != null){
	        	if(l1.val <= l2.val){
					prev.next = l1;
					l1 = l1.next;
				}
	        	else{
	        		prev.next = l2;
	        		l2 = l2.next;
	        	}
	        	prev = prev.next;
	        }
	        if(l1 != null)
	        	prev.next = l1;
	        if(l2 != null)
	        	prev.next = l2;
	        
	        return result.next;
			
		}

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = { 1, 3, 5, 7, 9 };
		int[] b = { 2, 4, 6, 8 };

		Solution so = new Solution();
		for (int i = 0; i < a.length; i++) {
			so.buildList(so.header, a[i]);
		}
		ListNode l1 = so.header;
		
		so.header = null;
		
		for (int i = 0; i < b.length; i++) {
			so.buildList(so.header, b[i]);
		}
		
		ListNode l2 = so.header;
		
		so.printList(so.mergeTwoLists(l1, l2));
	}

}
