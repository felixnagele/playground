package io.github.felixnagele.shootergame;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JPanel;
import javax.swing.Timer;

public class GamePanel extends JPanel 
{

	/**
	 * Create the panel.
	 */
	public GamePanel() 
	{
		this.addKeyListener(new KeyInput());
		this.addMouseListener(new MouseInput());
		this.setFocusable(true);
		
		Timer timer = new Timer(10, new GameRender());
		timer.start();
	}

	protected void paintComponent(Graphics g) 
	{
		super.paintComponent(g);
		
		Graphics2D g2D = (Graphics2D)g;
		
		//Player
		g2D.setColor(Color.BLACK);
		g2D.fillRect(Var.playerX, Var.playerY, Var.playerWidth, Var.playerHeight);
		
		//Bullets
		g2D.setColor(Color.RED);
		for(Var.Bullet bullet : Var.bullets)
		{
			g2D.fillRect((int)bullet.x, (int)bullet.y, Var.bulletWidth, Var.bulletHeight);
		}
		
		repaint();
	}
	
	

}
