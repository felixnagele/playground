package io.github.felixnagele.clickmatter;

import java.util.Random;

public class Var
{
	public Var()
	{
		Methods.setBooleanArrayFalse(clicked);
		for(int i = 0; i < random.length; i++)
		{
			randomx[i] = rng.nextInt(generatewidth+1);
			randomy[i] = rng.nextInt(generateheight+1);
		}
	}
	public static Random rng = new Random();

	public static int screenwidth = 1920;
	public static int screenheight = 1080;
	public static int objw = 50;
	public static int objh = 50;
	public static int generatewidth = screenwidth - objw;
	public static int generateheight = screenheight - objh;
	public static int mousex;
	public static int mousey;
	public static int randomobjnumber = 10;
	public static int[] random = new int[randomobjnumber];
	public static int[] randomx = new int[randomobjnumber];
	public static int[] randomy = new int[randomobjnumber];
	public static boolean[] clicked = new boolean[randomobjnumber];
	public static int clickedcount = 0;
	public static int gametime;
	public static long entertime;
	public static boolean gameactive = true;
	public static boolean mouseinpanel = false;

}
