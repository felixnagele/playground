package io.github.felixnagele.clickmatter;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JPanel;

public class Paint extends JPanel
{
	/**
	 * Create the panel.
	 */
	public Paint()
	{
		this.addMouseListener(new MouseAnimation());
		this.addMouseMotionListener(new MouseAnimation());
	}

	protected void paintComponent(Graphics g)
	{
		super.paintComponent(g);
		Graphics2D g2D = (Graphics2D)g;

		int x = this.getWidth();
		int y = this.getHeight();

		if(Var.gameactive)
		{
			for(int i = 0; i < Var.random.length; i++)
			{
				if(Var.clicked[i])
				{
					g2D.setColor(Color.CYAN);
					g2D.fillRect(Var.randomx[i], Var.randomy[i], Var.objw, Var.objh);
				}
				else
				{
					g2D.setColor(Color.BLUE);
					g2D.fillRect(Var.randomx[i], Var.randomy[i], Var.objw, Var.objh);
				}
			}
		}
		else
		{
			g2D.setColor(Color.RED);
			Font font = new Font("",Font.BOLD,50);
			g2D.setFont(font);
			g2D.drawString("Mighty Win", x/2-250, y/2);
		}

		g2D.setColor(Color.BLACK);
		g2D.drawLine(Var.mousex-15, Var.mousey, Var.mousex+15, Var.mousey);
		g2D.drawLine(Var.mousex, Var.mousey-15, Var.mousex, Var.mousey+15);

		for(int i = 0; i < Var.clicked.length; i++)
		{
			if(Var.clicked[i])
			{
				Var.clickedcount++;
			}
			if(Var.clickedcount == Var.randomobjnumber)
			{
				Var.gameactive = false;
				Var.clickedcount = 0;
			}
		}
		Var.clickedcount = 0;
		repaint();
	}



}
