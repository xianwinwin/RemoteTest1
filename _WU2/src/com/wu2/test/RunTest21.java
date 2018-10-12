package com.wu2.test;

public class RunTest21
{
	public static void main(String args[])
	{		
		System.out.println("start x-001");
		long start = System.currentTimeMillis();
		
		System.out.println("program starts...");
		
		Thread t = new Thread(new Worker());
		t.start();
		try
		{
			t.join();
		} catch (InterruptedException e)
		{ 
			System.out.println("X219..c this is me after revisions! 3");
		}
		
		long end = System.currentTimeMillis();		
		System.out.println("ended in "+(end-start)/1000.0+" seconds");
	}
}
