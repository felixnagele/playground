package io.github.felixnagele.clickmatter;

import java.awt.BorderLayout;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class Frame extends JFrame
{
	/**
	 * Create the frame.
	 */
	public Frame()
	{
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(0, 0, Var.screenwidth, Var.screenheight);
		this.setUndecorated(true);
		this.setExtendedState(MAXIMIZED_BOTH);
		this.setIconImage(new ImageIcon("rsc/ClickMatter_Icon.png").getImage());

		Paint paint = new Paint();
		getContentPane().add(paint, BorderLayout.CENTER);
	}

}
