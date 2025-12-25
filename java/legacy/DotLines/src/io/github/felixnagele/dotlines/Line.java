package io.github.felixnagele.dotlines;

import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;

public class Line
{
	private ArrayList<Dot> dlist = new ArrayList<Dot>();
	private Color color = Color.YELLOW;

	public void addDot(Dot d)
	{
		dlist.add(d);
	}

	public Dot getDot(int i)
	{
		if(i < 0 || i > dlist.size())
		{
			return null;
		}
		else
		{
			return dlist.get(i);
		}
	}

	public int size()
	{
		return dlist.size();
	}

	public void paint(Graphics g)
	{
		//LINE
		g.setColor(color);

		int[] x = new int[dlist.size()];
		int[] y = new int[dlist.size()];

		int n = 0;

		for(Dot temp : dlist)
		{
			x[n] = temp.getX();
			y[n] = temp.getY();
			n++;
		}
		g.drawPolyline(x, y, dlist.size());

		//DOT
		for (int i = 0; i < dlist.size(); i++)
		{
			dlist.get(i).paint(g);
		}
	}

	public void clear()
	{
		dlist.clear();
	}

	@Override
	public String toString()
	{
	    String out = "";
	    for (int i = 0; i < dlist.size(); i++)
	    {
	        out += dlist.get(i) + ";";
	    }
	    return out;
	}



}
