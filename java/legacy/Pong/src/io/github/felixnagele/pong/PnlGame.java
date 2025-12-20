package io.github.felixnagele.pong;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Random;

import javax.swing.JPanel;
import javax.swing.Timer;

public class PnlGame extends JPanel implements KeyListener, ActionListener
{
	Random rng = new Random();
	private Timer timer;
	private boolean activate = true;
	private int player1x = 5;
	private int player1y = 5;
	private int player1w = 10;
	private int player1h = 50;
	private int player2x;
	private int player2y = 5;
	private int player2w = 10;
	private int player2h = 50;
	private boolean player1up = false;
	private boolean player1down = false;
	private boolean player2up = false;
	private boolean player2down = false;
	private boolean start = false;
	private int ballx;
	private int bally;
	private int ballsize = 20;
	private int ballspeed = 3;
	private int player1count = 0;
	private int player2count = 0;
	private boolean startcollision = false;
	private boolean player1collision = false;
	private boolean player2collision = false;
	private int ballangle;
	private double ballVx;
	private double ballVy;

	public PnlGame()
	{
		this.addKeyListener(this);
		this.setFocusable(true);
		timer = new Timer(15,this);
		timer.start();
	}

	protected void paintComponent(Graphics g)
	{
		super.paintComponent(g);
		Graphics2D g2D = (Graphics2D)g;

		if(activate)
		{
			player2x = this.getWidth()-player2w-5;
			ballx = this.getWidth()/2-ballsize/2;
			bally = this.getHeight()/2-ballsize/2;
			activate = false;
		}

		g2D.setColor(Color.BLACK);
		g2D.fillRect(0, 0, getWidth(), getHeight());
		g2D.setColor(Color.WHITE);
		g2D.fillRect(player1x, player1y, player1w, player1h);
		g2D.fillRect(player2x, player2y, player2w, player2h);
		g2D.fillRect(ballx, bally, ballsize, ballsize);

		Font font = new Font("",Font.PLAIN,50);
		g2D.setFont(font);
		g2D.drawString(player1count+"", this.getWidth()/3, this.getHeight()/3);
		g2D.drawString(player2count+"", this.getWidth()/3+this.getWidth()/3-50/2, this.getHeight()/3);
		g2D.drawString(":", this.getWidth()/3+77, this.getHeight()/3);

		if(player1y + player1h >= this.getHeight())
		{
			player1y = this.getHeight()-player1h;
		}
		if(player1y <= 0)
		{
			player1y = 0;
		}
		if(player2y + player2h >= this.getHeight())
		{
			player2y = this.getHeight()-player2h;
		}
		if(player2y <= 0)
		{
			player2y = 0;
		}
		if(ballx + ballsize >= this.getWidth())
		{
			player1count++;
			start = false;
			ballx = this.getWidth()/2-ballsize/2;
			bally = this.getHeight()/2-ballsize/2;
		}
		if(ballx + ballsize <= 0)
		{
			player2count++;
			start = false;
			ballx = this.getWidth()/2-ballsize/2;
			bally = this.getHeight()/2-ballsize/2;
		}
		repaint();
	}

	public void actionPerformed(ActionEvent e)
	{
		if(start && !startcollision)
		{
			ballangle = rng.nextInt(120+1)-60;
			double radians = Math.toRadians(ballangle);
			ballVx = ballspeed*Math.cos(radians);
			ballVy = ballspeed*Math.sin(radians);
			startcollision = true;
		}
		if(start)
		{
			ballx += ballVx;
			bally += ballVy;
		}
		if(player1up)
		{
			player1y -= 5;
		}
		if(player1down)
		{
			player1y += 5;
		}
		if(player2up)
		{
			player2y -= 5;
		}
		if(player2down)
		{
			player2y += 5;
		}
		if(bally <= 0 || bally + ballsize >= this.getHeight())
		{
			ballVy = -ballVy;
		}
		if(collision(ballx, bally, player2x, player2y, player2w, player2h) ||
		   collision(ballx+ballsize, bally, player2x, player2y, player2w, player2h) ||
		   collision(ballx+ballsize, bally+ballsize, player2x, player2y, player2w, player2h) ||
		   collision(ballx, bally+ballsize, player2x, player2y, player2w, player2h))
		{
			if(ballVx > 0)
			{
				ballVx = -ballVx;
			}
		}
		if(collision(ballx, bally, player1x, player1y, player1w, player1h) ||
		   collision(ballx+ballsize, bally, player1x, player1y, player1w, player1h) ||
		   collision(ballx+ballsize, bally+ballsize, player1x, player1y, player1w, player1h) ||
		   collision(ballx, bally+ballsize, player1x, player1y, player1w, player1h))
		{
			if(ballVx < 0)
			{
				ballVx = -ballVx;
			}
		}
		repaint();
	}

	public void keyPressed(KeyEvent e)
	{
		int key = e.getKeyCode();

		if(key == KeyEvent.VK_W)
		{
			player1up = true;
		}
		else if(key == KeyEvent.VK_S)
		{
			player1down = true;
		}
		else if(key == KeyEvent.VK_UP)
		{
			player2up = true;
		}
		else if(key == KeyEvent.VK_DOWN)
		{
			player2down = true;
		}
		else if(key == KeyEvent.VK_SPACE)
		{
			start = true;
		}
		repaint();
	}

	public void keyReleased(KeyEvent e)
	{
		int key = e.getKeyCode();

		if(key == KeyEvent.VK_W)
		{
			player1up = false;
		}
		else if(key == KeyEvent.VK_S)
		{
			player1down = false;
		}
		else if(key == KeyEvent.VK_UP)
		{
			player2up = false;
		}
		else if(key == KeyEvent.VK_DOWN)
		{
			player2down = false;
		}
		repaint();
	}

	public void keyTyped(KeyEvent e)
	{
		// TODO Auto-generated method stub

	}

	public static boolean collision(int xP, int yP, int xR, int yR, int w, int h)
	{
		return xP >= xR && xP <= (xR + w) && yP >= yR && yP <= (yR + h);
	}
}
