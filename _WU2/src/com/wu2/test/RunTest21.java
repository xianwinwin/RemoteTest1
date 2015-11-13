package com.wu2.test;

public class RunTest21
{
	public static void main(String args[])
	{		
		System.out.println("start x-3783");
		long start = System.currentTimeMillis();
		
		System.out.println("program starts...");
		
		Thread t = new Thread(new Worker());
		t.start();
		
		long end = System.currentTimeMillis();		
		System.out.println("ended in "+(end-start)/1000.0+" seconds");
	}
}
