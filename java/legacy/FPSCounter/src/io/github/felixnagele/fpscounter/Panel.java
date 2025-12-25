package io.github.felixnagele.fpscounter;

import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Panel extends JPanel implements ActionListener
{
	Timer timer = new Timer(1, this);
	int x = 0;
	int y = 0;
	int sizeX = 50;
	int sizeY = 50;
	boolean right = false;
	boolean left = true;
	int fps = 0;
	long lastFpsCheck = System.nanoTime();
	int countedFrames = 0;

	public Panel()
	{
		this.timer.start();
	}

	protected void paintComponent(Graphics g)
	{
		super.paintComponent(g);
		this.y = (getHeight() / 2 - 50);

		this.countedFrames += 1;
		if (System.nanoTime() > this.lastFpsCheck + 1000000000L)
		{
			this.lastFpsCheck = System.nanoTime();
			this.fps = this.countedFrames;
			this.countedFrames = 0;

			System.out.println("FPS = " + this.fps);
		}
		if (this.x <= 0)
		{
			this.right = true;
			this.left = false;
		}
		if (this.x >= getWidth() - this.sizeX)
		{
			this.right = false;
			this.left = true;
		}
		g.fillRect(this.x, this.y, this.sizeX, this.sizeY);
		g.setFont(new Font("TimesRoman", 0, 40));
		g.drawString("FPS: " + this.fps, 5, 30);
		repaint();
	}

	public void actionPerformed(ActionEvent e)
	{
		if (this.right)
		{
			this.x += 5;
		}
		if (this.left)
		{
			this.x -= 5;
		}
	}
}
