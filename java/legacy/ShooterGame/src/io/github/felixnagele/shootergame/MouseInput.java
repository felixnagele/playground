package io.github.felixnagele.shootergame;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class MouseInput implements MouseListener
{
	public void mouseClicked(MouseEvent e)
	{

	}
	public void mousePressed(MouseEvent e)
	{
		int mX = e.getX();
		int mY = e.getY();

		float startX = Var.playerX + Var.playerWidth/2 - Var.bulletWidth/2;
		float startY = Var.playerY + Var.playerHeight/2 - Var.bulletHeight/2;

		float angle = (float) Math.atan2(mY - Var.playerY, mX - Var.playerX);

		float bulVelX = (float) ((Var.bulletVel) * Math.cos(angle));
		float bulVelY = (float) ((Var.bulletVel) * Math.sin(angle));

		Var.bullets.add(new Var.Bullet(startX, startY, bulVelX, bulVelY));
	}
	public void mouseReleased(MouseEvent e)
	{
	}
	public void mouseEntered(MouseEvent e) {
	}
	public void mouseExited(MouseEvent e) {
	}
}
