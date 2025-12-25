package io.github.felixnagele.viruskiller;

import javax.swing.Timer;

public class Var
{

	public Var()
	{
	}

	public static Timer timer;
	public static final int framewidth = 800;
	public static final int frameheight = 800;
	public static int delta = 30;
	public static boolean start = false;
	public static boolean end = false;
	public static boolean outofmap = false;
	public static boolean[] outofmapbool = new boolean[delta];
	public static int enemiew = 50;
	public static int enemieh = 50;
	public static int[] enemiex = new int[delta];
	public static int[] enemiey = new int[delta];
	public static boolean color = false;
	public static int mousex;
	public static int mousey;
	public static boolean[] clicked = new boolean[delta];
	public static int clickcount = 0;
	public static boolean endscore = false;

}
