package io.github.felixnagele.viruskiller;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class Main extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Main frame = new Main();
					frame.setVisible(true);
					new KeyHandler();
					new Animation();
					new MouseHandler();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Main() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, Var.framewidth, Var.frameheight);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(0, 0, 0, 0));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
		this.setLocationRelativeTo(null);
		this.setBackground(Color.BLACK);
		this.setResizable(false);
		this.setIconImage(loadImage("rsc/VirusKiller_Icon.png"));

		Paint paint = new Paint();
		contentPane.add(paint, BorderLayout.CENTER);
	}

	public static BufferedImage loadImage(String path)
	{
		BufferedImage picture = null;
		try
		{
		    File file = new File(path);
			picture = ImageIO.read(file);
		}
		catch (IOException e)
		{
			e.printStackTrace();
			System.out.println("Could not load pictures!");
		}
		return picture;
	}

}
