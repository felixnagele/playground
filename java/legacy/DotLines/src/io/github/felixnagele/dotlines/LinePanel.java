package io.github.felixnagele.dotlines;

import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;

import javax.swing.JPanel;

public class LinePanel extends JPanel implements MouseListener
{
	private ArrayList<Dot> dlist = new ArrayList<Dot>();
	private Line line = new Line();

	/**
	 * Create the panel.
	 */
	public LinePanel()
	{
		this.addMouseListener(this);
	}

	public LinePanel(Line line)
	{
		this.line = line;
		this.addMouseListener(this);
	}

	public Line getLine()
	{
		return line;
	}

	@Override
	protected void paintComponent(Graphics g)
	{
		super.paintComponent(g);

		if (line != null)
		{
			line.paint(g);
		}
	}

	@Override
	public void mouseClicked(MouseEvent e)
	{

	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mousePressed(MouseEvent e) {
		if(e.getButton() == MouseEvent.BUTTON1)
		{
			Dot dot = new Dot();
			dot.setX(e.getX());
			dot.setY(e.getY());

			if (line == null)
			{
				line = new Line();
			}
			else
			{
				line.addDot(dot);
			}

			System.out.println("DOT: "+dot);
			System.out.println();
			System.out.println("LINE: "+line);
			repaint();
		}
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub

	}
}
