package io.github.felixnagele.shootergame;

import java.awt.Toolkit;
import java.util.ArrayList;

public class Var
{

	public Var()
	{

	}

	//Frame
	public static final int FRAME_WIDTH = Toolkit.getDefaultToolkit().getScreenSize().width;
	public static final int FRAME_HEIGHT = Toolkit.getDefaultToolkit().getScreenSize().height;
	//Player
	public static int playerWidth = 50;
	public static int playerHeight = 50;
	public static int playerX = FRAME_WIDTH/2 - playerWidth/2;
	public static int playerY = FRAME_HEIGHT/2 - playerHeight/2;
	public static float plVel = 1;
	//Bullet
	public static int bulletWidth = 10;
	public static int bulletHeight = 10;
	public static int bulletVel = 7;
	public static ArrayList<Bullet> bullets = new ArrayList<Bullet>();
	//Mouse
	public static boolean mouseClicked = false;
	//Keys





	public static boolean[] keys = new boolean[4];

	public static class Bullet
	{
		public float x;
		public float y;
		public float velX;
		public float velY;

		public Bullet(float x, float y, float velX, float velY)
		{
			this.x = x;
			this.y = y;
			this.velX = velX;
			this.velY = velY;
		}
	}
}
