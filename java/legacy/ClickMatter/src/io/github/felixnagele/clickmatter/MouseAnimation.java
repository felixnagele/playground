package io.github.felixnagele.clickmatter;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

public class MouseAnimation implements MouseMotionListener, MouseListener
{

	public MouseAnimation()
	{
	}

	public void mouseMoved(MouseEvent e)
	{
		Var.mousex = e.getX();
		Var.mousey = e.getY();
	}
	public void mouseEntered(MouseEvent e)
	{
		Var.mouseinpanel = true;
	}
	public void mouseClicked(MouseEvent e)
	{

	}

	// ***************************************************

	public void mouseExited(MouseEvent e)
	{

	}


	public void mousePressed(MouseEvent e)
	{
		Var.mousex = e.getX();
		Var.mousey = e.getY();

		for(int i = 0; i < Var.random.length; i++)
		{
			if(Methods.collision(Var.mousex, Var.mousey, Var.randomx[i], Var.randomy[i], Var.objw, Var.objh))
			{
				Var.clicked[i] = true;
			}
		}
	}


	public void mouseReleased(MouseEvent e)
	{

	}


	public void mouseDragged(MouseEvent e)
	{
		Var.mousex = e.getX();
		Var.mousey = e.getY();
	}


}
