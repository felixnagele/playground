package io.github.felixnagele.spaceinvadersx;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JPanel;
import javax.swing.Timer;

public class Draw extends JPanel implements KeyListener, ActionListener
{
	Timer timer;
	private int moveX = 225;
	private int moveY;
	private int speed = 4;
	private int shotspeed = 5;
	private int shotX;
	private int shotY;
	private int shotWidth = 4;
	private int shotHeight = 10;
	private int[] enemieX;
	private double[] enemieY;
	private int enemieWidth = 30;
	private int enemieHeight = 20;
	private boolean shot = false;
	private boolean moveLeft = false;
	private boolean moveRight = false;
	private int delta = 1;
	private int enemiecount = 0;
	private boolean startGame = true;
	private boolean collision = false;

	/**
	 * Create the panel.
	 */
	public Draw()
	{
		timer = new Timer(15,this);
		timer.start();
		enemieX = new int[30];
		enemieY = new double[30];
		for(int i = 0; i < 10; i++)
		{
			for(int j = 0; j < 3; j++)
			{
		        this.enemieX[(j * 10 + i)] = (10 + i * 40);
		        this.enemieY[(j * 10 + i)] = (10 + j * 50);
			}
		}

	}

	protected void paintComponent(Graphics g)
	{
		moveY = getHeight()-30;
		super.paintComponent(g);
		Graphics2D g2D = (Graphics2D)g;

		if(startGame)
		{
			//PLAYER
			g2D.setColor(Color.GREEN);
			g2D.fillRect(moveX-40/2, moveY, 40, 30);
			for(int i = 0; i < enemieX.length; i++)
			{
				if(collision(moveX-40/2, moveY, enemieX[i], (int)enemieY[i], enemieWidth, enemieHeight))
				{
					startGame = false;
				}
			}

			//ENEMIES
			for(int i = 0; i < enemieX.length; i++)
			{
				g2D.setColor(Color.WHITE);
				g2D.fillRect(enemieX[i], (int)enemieY[i], enemieWidth, enemieHeight);
			}

			for(int i = 0; i < enemieX.length; i++)
			{
				if(collision(shotX, shotY, enemieX[i],(int)enemieY[i], enemieWidth, enemieHeight))
				{
					enemiecount++;
				}
				if(enemieY[i]+enemieHeight >= this.getHeight())
				{
					startGame = false;
				}
			}

			//SHOT
			if(shot)
			{
				g2D.setColor(Color.RED);
				g2D.fillRect(shotX-shotWidth/2, shotY, shotWidth, shotHeight);
			}
			else
			{
				shotX = moveX + shotWidth/2;
				shotY = moveY + shotHeight/2;
			}
			while(collision)
			{
				shot = false;
			}
			if(border(shotY,0))
			{
				shot = false;
			}
			for(int i = 0; i < enemieX.length; i++)
			{
				if(collision(shotX, shotY, enemieX[i],(int)enemieY[i], enemieWidth, enemieHeight))
				{
					enemieX[i] = -100;
					enemiecount++;
					collision = true;
				}
				collision = false;
			}
			if(enemiecount == 60)
			{
				startGame = false;
			}
		}
		else
		{
			Font font = new Font("",Font.BOLD,70);
			g2D.setColor(Color.BLACK);
			g2D.fillRect(0, 0, 800, 800);
			g2D.setColor(Color.WHITE);
			g2D.setFont(font);
			g2D.drawString("GAME OVER", this.getWidth()/2-210, this.getHeight()/2);
		}
		repaint();
	}

	public void keyPressed(KeyEvent e)
	{
		int key = e.getKeyCode();

		if(key == KeyEvent.VK_A)
		{
			moveLeft = true;
		}
		else if(key == KeyEvent.VK_D)
		{
			moveRight = true;
		}
		else if(key == KeyEvent.VK_SPACE)
		{
			shot = true;
		}
		repaint();
	}

	public void keyReleased(KeyEvent e)
	{
		int key = e.getKeyCode();

		if(key == KeyEvent.VK_A)
		{
			moveLeft = false;
		}
		else if(key == KeyEvent.VK_D)
		{
			moveRight = false;
		}
	}
	public void keyTyped(KeyEvent e)
	{
	}

	public void actionPerformed(ActionEvent e)
	{
		//SHOT
		if(shot)
		{
			shotY-=shotspeed;
		}

		//PLAYER
		if(moveRight)
		{
			moveX += speed;
		}
		if(moveLeft)
		{
			moveX -= speed;
		}

		//ENEMIES
		for(int i = 0; i < enemieX.length; i++)
		{
			if(enemieXBorderMax(enemieX[i]+enemieWidth, 450))
			{
				delta = -1;
			}
			if(enemieXBorderZero(enemieX[i], 0))
			{
				delta = 1;
			}
		}
		for(int i = 0; i < enemieX.length; i++)
		{
			if(enemieX[i] > -100)
			{
				enemieX[i]+=delta;
				enemieY[i]+=0.037;
			}
		}
	}
	public static boolean border(int shotY, int maxheight)
	{
		return shotY <= maxheight;
	}
	public static boolean enemieXBorderZero(int enemieX, int zero)
	{
		return enemieX <= zero;
	}
	public static boolean enemieXBorderMax(int enemieX, int maxwidth)
	{
		return enemieX >= maxwidth;
	}
	public static boolean collision(int shotX, int shotY, int enemieX, int enemieY, int enemieWidth, int enemieHeight)
	{
		return(shotY <= enemieY + enemieHeight && shotY >= enemieY)&&(shotX <= enemieX + enemieWidth && shotX >= enemieX);
	}
}
