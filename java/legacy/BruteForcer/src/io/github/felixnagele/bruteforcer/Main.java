package io.github.felixnagele.bruteforcer;

import java.util.Random;

public class Main
{

	public static void main(String[] args)
	{
		Random rng = new Random();
		int max = 999999999;
		int min = 100000000;
		int password = 584292301;
		int passwordX = 0;
		long timeStart = System.nanoTime();
		long timeNow = 0;

		for(int i = 0; i <= max; i++)
		{
			passwordX = rng.nextInt(max-min+1)+min;
			//System.out.println(passwordX);
			if(passwordX == password)
			{
				timeNow = System.nanoTime() - timeStart;

				System.out.println("Password is "+passwordX);
				System.out.println("Time: "+timeNow*Math.pow(10, -9)+"sec");
				break;
			}
		}
	}

}
