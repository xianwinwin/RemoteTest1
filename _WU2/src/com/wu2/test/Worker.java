package com.wu2.test;

public class Worker implements Runnable
{

	@Override
	public void run()
	{
		//WOW this is dude 2
		System.out.println(Thread.currentThread().getName());
		
	}
}