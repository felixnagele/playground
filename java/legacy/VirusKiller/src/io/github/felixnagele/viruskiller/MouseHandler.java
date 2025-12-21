package io.github.felixnagele.viruskiller;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

public class MouseHandler implements MouseMotionListener, MouseListener
{

	public MouseHandler()
	{
		setBooleanArrayFalse(Var.clicked);
	}


	public void mouseMoved(MouseEvent e)
	{
		Var.mousex = e.getX();
		Var.mousey = e.getY();
	}
	public void mouseClicked(MouseEvent e)
	{
		Var.mousex = e.getX();
		Var.mousey = e.getY();
	}

	public void mouseEntered(MouseEvent e)
	{

	}

	public void mouseExited(MouseEvent e)
	{

	}

	public void mousePressed(MouseEvent e)
	{
		for(int i = 0; i < Var.enemiex.length; i++)
		{
			if(collision(Var.mousex, Var.mousey, Var.enemiex[i], Var.enemiey[i], Var.enemiew, Var.enemieh))
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
	public static boolean collision(int xP, int yP, int xR, int yR, int w, int h)
	{
		return (xP >= xR && xP <= (xR + w)) && (yP >= yR && yP <= (yR + h));
	}
	public static boolean[] setBooleanArrayFalse(boolean[] a)
	{
		for(int i = 0; i < a.length; i++)
		{
			a[i] = false;
		}
		return a;
	}
	public static boolean[] setBooleanArrayTrue(boolean[] a)
	{
		for(int i = 0; i < a.length; i++)
		{
			a[i] = true;
		}
		return a;
	}


}
