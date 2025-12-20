package io.github.felixnagele.rollingdice;

import java.awt.Graphics;

import javax.swing.JPanel;

import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.List;

public class DicePanel extends JPanel
{
	// Dice[] dices = new Dice[amount];	- Normal Array

	List<Dice> dices = new ArrayList<Dice>();

	/**
	 * Create the panel.
	 */
	public DicePanel()
	{

		initComponents();
	}
	private void initComponents() {
		addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent arg0) {
				thisMouseClicked(arg0);
			}
		});
	}

	@Override
	protected void paintComponent(Graphics g)
	{
		super.paintComponent(g);

//		for (int i = 0; i < dices.length; i++) - Normal Array
//		{
//			dices[i].paint(g);
//		}

		for (int i = 0; i < dices.size(); i++)
		{
			Dice d = dices.get(i);
			d.paint(g);
		}
		repaint();
	}

	protected void thisMouseClicked(MouseEvent e)
	{
		if(e.getButton() == MouseEvent.BUTTON1)
		{
			Point p = new Point(e.getX(), e.getY());
			Dice d = new Dice(p);

			// dices[x] = d; - Normal Array
			dices.add(d);	// For adding objects to the list

		}

		if(e.getButton() == MouseEvent.BUTTON3)
		{
			for (Dice d : dices)
			{
				d.roll();
			}
		}

		repaint();
	}
}
