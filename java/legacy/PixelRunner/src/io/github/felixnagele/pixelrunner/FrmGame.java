package io.github.felixnagele.pixelrunner;


import java.awt.EventQueue;
import java.awt.Toolkit;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import java.awt.BorderLayout;
import java.awt.Color;



public class FrmGame extends JFrame
{
	/**
	 * Launch the application.
	 */
	public static void main(String[] args)
	{
		EventQueue.invokeLater(new Runnable()
		{
			public void run()
			{
				try
				{
					FrmGame frame = new FrmGame();
					frame.setVisible(true);
				}
				catch (Exception e)
				{
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public FrmGame()
	{
		initComponents();
	}
	public void initComponents() {
		int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
		int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;
		int windowSize = Math.min(screenWidth, screenHeight) * 3 / 4;

		setTitle("Pixel-Runner");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, windowSize, windowSize);
		setIconImage(new ImageIcon("rsc/Pixel-Runner_Icon.png").getImage());

		PnlGame pnlGame = new PnlGame();
		pnlGame.setBackground(Color.BLACK);
		getContentPane().add(pnlGame, BorderLayout.CENTER);
		this.addKeyListener(pnlGame);
	}
}
