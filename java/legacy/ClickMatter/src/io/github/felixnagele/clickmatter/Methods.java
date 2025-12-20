package io.github.felixnagele.clickmatter;

public class Methods 
{

	public Methods() 
	{
		
	}
	public static boolean[] setBooleanArrayFalse(boolean[] a)
	{
		for(int i = 0; i < a.length; i++)
		{
			a[i] = false;
		}
		return a;
	}
	public static boolean collision(int xP, int yP, int xR, int yR, int w, int h)
	{
		return (xP >= xR && xP <= (xR + w)) && (yP >= yR && yP <= (yR + h));
	}

}
