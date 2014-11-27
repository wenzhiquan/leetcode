package com.wen.triangle;

import java.util.ArrayList;
import java.util.List;

public class Solution {
	
    public int minimumTotal(List<List<Integer>> triangle) {
    	if(triangle.size() == 0) return 0;
    	if(triangle.size() == 1) return triangle.get(0).get(0);
    	   	
    	int result = triangle.get(0).get(0);
    	int index = 0;
    	
    	for(int i=1;i<triangle.size();i++){
    		if(triangle.get(i).get(index) < triangle.get(i).get(index+1))
    			result += triangle.get(i).get(index);
    		else{
    			result += triangle.get(i).get(index+1);
    			index++;
    		}
    	}
    	
		return result;
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution so = new Solution();
		List<List<Integer>> triangle = new ArrayList<List<Integer>>();
//		List<Integer> a = new ArrayList<Integer>();
//		a.add(2);
//		triangle.add(a);
//		a = new ArrayList<Integer>();
//		a.add(0, 4);
//		a.add(0, 3);
//		triangle.add(a);
//		a = new ArrayList<Integer>();
//		a.add(0, 7);
//		a.add(0, 5);
//		a.add(0, 6);
//		triangle.add(a);
//		a = new ArrayList<Integer>();
//		a.add(0, 3);
//		a.add(0, 8);
//		a.add(0, 1);
//		a.add(0, 4);
//		triangle.add(a);
		
		List<Integer> b = new ArrayList<Integer>();
		b.add(-1);
		triangle.add(b);
		b = new ArrayList<Integer>();
		b.add(0, 3);
		b.add(0, 2);
		triangle.add(b);
		b = new ArrayList<Integer>();
		b.add(0, -3);
		b.add(0, -1);
		b.add(0, 1);
		triangle.add(b);
		
		for(int i = 0;i<triangle.size();i++)
			System.out.println(triangle.get(i));
		
		System.out.println(so.minimumTotal(triangle));
	}

}
