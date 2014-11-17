package com.wen.minStack;

import java.util.Stack;

public class Solution {
	
	private long min;
	private Stack<Long> stack = new Stack<Long>();
	
	public void push(int x) {
		if(this.stack.size() == 0){
			this.stack.push((long)x);
			this.min = x;
		}
		else{
			this.stack.push(x-this.min);
			if(x<this.min) this.min = x;
		}
	}

    public void pop() {
        if(this.stack.size() > 0){
        	long pop = this.stack.pop();
        	if(pop < 0) this.min -= pop;
        }
    }

    public int top() {
        long top = this.stack.peek();
        if(this.stack.size() == 1)
        	return (int)top;
        else if(top < 0)
        	return (int)this.min;
        else
        	return (int)(this.min+top);
    }

    public int getMin() {
		return (int)this.min;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		so.push(2147483646);
		so.push(2147483646);
		so.push(2147483647);
		
		System.out.println(so.top());
		so.pop();
		System.out.println(so.getMin());
		so.pop();
		System.out.println(so.getMin());
		so.pop();
		so.push(2147483647);
		
		System.out.println(so.top());
		System.out.println(so.getMin());
		so.push(-2147483648);
		System.out.println(so.top());
		System.out.println(so.getMin());
		so.pop();
		System.out.println(so.getMin());
	}

}
