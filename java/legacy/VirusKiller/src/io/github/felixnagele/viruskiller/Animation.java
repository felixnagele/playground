package io.github.felixnagele.viruskiller;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Animation implements ActionListener
{

	public Animation()
	{
	}

	public void actionPerformed(ActionEvent e)
	{
		if(Var.start)
		{
			for(int i = 0; i < Var.enemiex.length; i++)
			{
				Var.enemiey[i]++;
				if(Var.enemiey[i] + Var.enemieh >= Var.frameheight)
				{
					if(Var.clicked[i])
					{
						Var.outofmapbool[i] = false;
					}
					else
					{
						Var.outofmapbool[i] = true;
					}
				}
			}
		}
	}
}
