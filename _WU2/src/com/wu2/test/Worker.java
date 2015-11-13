package com.wu2.test;

public class Worker implements Runnable
{

	@Override
	public void run()
	{
		System.out.println(Thread.currentThread().getName());
		
	}
}