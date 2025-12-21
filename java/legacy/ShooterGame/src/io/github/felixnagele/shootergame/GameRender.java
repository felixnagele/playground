package io.github.felixnagele.shootergame;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class GameRender implements ActionListener
{
	public void actionPerformed(ActionEvent e)
	{
		for(int i = 0; i < Var.keys.length; i++)
		{
			//Keys
			if(Var.keys[0] == true){Var.playerY -= Var.plVel;}
			if(Var.keys[1] == true){Var.playerX -= Var.plVel;}
			if(Var.keys[2] == true){Var.playerY += Var.plVel;}
			if(Var.keys[3] == true){Var.playerX += Var.plVel;}

			//Bullets
			ArrayList<Var.Bullet> toRemove = new ArrayList<Var.Bullet>();
			for(Var.Bullet bullet : Var.bullets)
			{
				bullet.x += bullet.velX;
				bullet.y += bullet.velY;

				if(bullet.x <= 0 || bullet.y <= 0 || bullet.x >= Var.FRAME_WIDTH || bullet.y >= Var.FRAME_HEIGHT)
				{
					toRemove.add(bullet);
				}
			}
			Var.bullets.removeAll(toRemove);

			if(Var.playerX <= 0)
			{
				Var.playerX = 0;
			}
			if(Var.playerY <= 0)
			{
				Var.playerY = 0;
			}
			if(Var.playerX >= Var.FRAME_WIDTH-Var.playerWidth)
			{
				Var.playerX = Var.FRAME_WIDTH-Var.playerWidth;
			}
			if(Var.playerY >= Var.FRAME_HEIGHT-Var.playerHeight)
			{
				Var.playerY = Var.FRAME_HEIGHT-Var.playerHeight;
			}
		}
	}
}
