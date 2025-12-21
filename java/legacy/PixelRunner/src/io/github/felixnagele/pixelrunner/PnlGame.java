package io.github.felixnagele.pixelrunner;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JPanel;

public class PnlGame extends JPanel implements KeyListener
{
	private int x = 0, y = 0;
	private int xs = 50, ys = 50;
	private boolean initialized = false;
	/**
	 * Create the panel.
	 */
	public PnlGame()
	{

	}

	protected void paintComponent(Graphics g)
	{
		super.paintComponent(g);

		if(!initialized)
		{
			x = this.getWidth() / 2 - xs / 2;
			y = this.getHeight() / 2 - ys / 2;
			initialized = true;
		}

		Graphics2D g2D = (Graphics2D)g;
		g2D.setColor(Color.WHITE);
		g2D.fillOval(x, y, xs, ys);
		this.repaint();
	}

	public void keyPressed(KeyEvent e)
	{
		if (e.getKeyCode() == KeyEvent.VK_D)
		{
			x+=5;
		}
		else if (e.getKeyCode() == KeyEvent.VK_A)
		{
			x-=5;
		}
		else if (e.getKeyCode() == KeyEvent.VK_W)
		{
			y-=5;
		}
		else if (e.getKeyCode() == KeyEvent.VK_S)
		{
			y+=5;
		}
		else if (e.getKeyCode() == KeyEvent.VK_UP)
		{
			xs+=50;
			ys+=50;
		}
		else if (e.getKeyCode() == KeyEvent.VK_DOWN)
		{
			xs-=50;
			ys-=50;
		}
		else if (e.getKeyCode() == KeyEvent.VK_ESCAPE)
		{
			System.exit(0);
		}
	}

	public void keyReleased(KeyEvent arg0)
	{


	}

	public void keyTyped(KeyEvent arg0)
	{


	}



}
