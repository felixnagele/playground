package io.github.felixnagele.pixelrunner;

import java.awt.EventQueue;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.ImageIcon;
import javax.swing.JTextArea;
import java.awt.Font;
import javax.swing.UIManager;
import java.awt.Color;

public class FrmCredits extends JFrame
{

	private JPanel contentPane;
	private JTextArea tarCredits;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args)
	{
		try {
			UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsClassicLookAndFeel");
		} catch (Throwable e) {
			e.printStackTrace();
		}
		EventQueue.invokeLater(new Runnable()
		{
			public void run()
			{
				try
				{
					FrmCredits frame = new FrmCredits();
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
	public FrmCredits()
	{
		initComponents();
	}
	private void initComponents() {
		int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
		int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;
		int windowWidth = screenWidth / 6;
		int windowHeight = screenHeight / 3;

		setTitle("Credits");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, windowWidth, windowHeight);
		contentPane = new JPanel();
		contentPane.setBackground(Color.BLACK);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		setIconImage(new ImageIcon("rsc/Pixel-Runner_Icon.png").getImage());

		tarCredits = new JTextArea();
		tarCredits.setForeground(Color.WHITE);
		tarCredits.setBackground(Color.BLACK);
		tarCredits.setFont(new Font("Arial Nova", Font.BOLD | Font.ITALIC, 20));
		tarCredits.setEditable(false);
		tarCredits.setText("~Credits~"
						  + "\n"
						  + "\nAuthor Felix"
						  + "\nVersion 1.0"
						  + "\nDate 05.2018"
						  + "\nLanguage English"
						  + "\n"
						  + "\n~~~~~~~~~~~~~~~~~");
		tarCredits.setBounds(10, 11, windowWidth - 30, windowHeight - 50);
		contentPane.add(tarCredits);

	}
}
