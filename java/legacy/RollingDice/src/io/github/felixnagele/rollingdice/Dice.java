package io.github.felixnagele.rollingdice;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

public class Dice
{
	private Point position;
	private int number;
	private final int A = 40;
	Random rng = new Random();

	public Dice()
	{

	}

	public Dice(Point position, int number)
	{
		this.position = position;
		this.number = number;
	}

	public Dice(Point position)
	{
		this.position = position;
		roll();
	}

	public void roll()
	{
		number = rng.nextInt(6)+1; // Max - Min +1 + Min
	}

	public void paint(Graphics g)
	{
		g.translate(position.x - A/2, position.y - A/2); 		// Translate the origin
		g.setColor(Color.WHITE);
		g.fillRoundRect(0, 0, A, A, 10, 10);

		int x = (A/4)/2;		// Outer margin = x
		int a4 = A/4;
		int a2 = A/2;

		g.setColor(Color.RED);

		if(number == 1)
		{
			g.fillOval(a2-a4/2, a2-a4/2, a4, a4);
		}

		if(number == 2)
		{
			g.fillOval(a4-x, a2+a4-x, a4, a4);
			g.fillOval(a2+x, x, a4, a4);

		}

		if(number == 3)
		{
			g.fillOval(a2-a4/2, a2-a4/2, a4, a4);
			g.fillOval(a4-x, a2+a4-x, a4, a4);
			g.fillOval(a2+x, x, a4, a4);

		}

		if(number == 4)
		{
			g.fillOval(a4-x, a4-x, a4, a4);
			g.fillOval(a4-x, a2+a4-x, a4, a4);
			g.fillOval(a2+x, x, a4, a4);
			g.fillOval(a2+x, a2+x, a4, a4);
		}

		if(number == 5)
		{
			g.fillOval(a2-a4/2, a2-a4/2, a4, a4); 	// point in the middle
			g.fillOval(a4-x, a4-x, a4, a4);			// point top left
			g.fillOval(a4-x, a2+a4-x, a4, a4);		// point bottom left
			g.fillOval(a2+x, x, a4, a4);			// point top right
			g.fillOval(a2+x, a2+x, a4, a4);			// point bottom right
		}

		if(number == 6)
		{
			g.fillOval(a4-x, a4-x, a4, a4);
			g.fillOval(a4-x, a2+a4-x, a4, a4);
			g.fillOval(a2+x, x, a4, a4);
			g.fillOval(a2+x, a2+x, a4, a4);
			g.fillOval(x, a2-x, a4, a4);
			g.fillOval(a2+x, a2-x, a4, a4);
		}

		g.translate(-(position.x -A/2), -(position.y - A/2));
	}
}
