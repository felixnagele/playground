package io.github.felixnagele.viruskiller;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.util.Random;

import javax.swing.JPanel;
import javax.swing.Timer;

public class Paint extends JPanel
{
	Random rng = new Random();
	Font startScreen = new Font("", Font.PLAIN, 50);
	Font endScreen = new Font("", Font.PLAIN, 30);
	/**
	 * Create the panel.
	 */
	public Paint() 
	{
		for(int i = 0; i < Var.enemiex.length; i++)
		{
			Var.enemiex[i] = rng.nextInt(750+1);
			Var.enemiey[i] = rng.nextInt(800+1);
			Var.enemiey[i] = -Var.enemiey[i];
		}
		
		Var.timer = new Timer(10, new Animation());
		Var.timer.start();
		this.addKeyListener(new KeyHandler());
		this.addMouseListener(new MouseHandler());
		this.addMouseMotionListener(new MouseHandler());
		this.setBackground(Color.BLACK);
		this.setFocusable(true);
	}

	protected void paintComponent(Graphics g) 
	{
		super.paintComponent(g);
		Graphics2D g2D = (Graphics2D)g;
		
		int w = this.getWidth();
		int h = this.getHeight();
		
		if(!Var.start)
		{
			g2D.setColor(Color.BLACK);
			g2D.fillRect(0, 0, w, h);
			g2D.setColor(Color.ORANGE);
			g2D.setFont(startScreen);
			g2D.drawString("---> VirusKiller <---", w/2-200, h/3);
			g2D.setColor(Color.WHITE);
			g2D.setFont(endScreen);
			g2D.drawString("Press SPACE to start...", w/2-145, h/2);
		}
		if(Var.start)
		{
				for(int i = 0; i < Var.enemiex.length; i++)
				{
					if(Var.outofmapbool[i])
					{
						Var.end = true;
					}
					if(!Var.clicked[i])
					{
						g2D.setColor(Color.GREEN);
						g2D.fillRect(Var.enemiex[i], Var.enemiey[i], Var.enemiew, Var.enemieh);
					}
					if(Var.end)
					{
						g2D.setColor(Color.BLACK);
						g2D.fillRect(0, 0, w, h);
						g2D.setColor(Color.RED);
						g2D.setFont(endScreen);
						g2D.drawString("VIRUS DEFENDER FAILED", w/2-160, h/2);
					}
				}
		}
		else if(!Var.start && Var.endscore)
		{
			g2D.setColor(Color.BLACK);
			g2D.fillRect(0, 0, w, h);
			g2D.setColor(Color.GREEN);
			g2D.setFont(endScreen);
			g2D.drawString("VIRUS DEFENDER SUCCESSFUL", w/2-220, h/2);
		}

		g2D.setColor(Color.WHITE);
		g2D.drawLine(Var.mousex-20, Var.mousey, Var.mousex+20, Var.mousey);
		g2D.drawLine(Var.mousex, Var.mousey-20, Var.mousex, Var.mousey+20);
		
		for(int i = 0; i < Var.enemiex.length; i++)
		{
			if(Var.clicked[i])
			{
				Var.clickcount++;
			}
			if(Var.clickcount == Var.delta)
			{
				Var.start = false;
				Var.endscore = true;
			}
		}
		Var.clickcount = 0;
		
		repaint();
	}
	
	

}
