package io.github.felixnagele.pixelrunner;

import java.awt.EventQueue;
import java.awt.Toolkit;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import java.awt.Font;
import javax.swing.UIManager;
import java.awt.Color;

public class FrmInfos extends JFrame
{

	private JPanel contentPane;
	private JTextArea tarInfos;

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
					FrmInfos frame = new FrmInfos();
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
	public FrmInfos()
	{
		initComponents();
	}
	private void initComponents() {
		int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
		int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;
		int windowWidth = screenWidth / 4;
		int windowHeight = screenHeight / 3;

		setTitle("Infos");
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setBounds(100, 100, windowWidth, windowHeight);
		contentPane = new JPanel();
		contentPane.setBackground(Color.BLACK);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		setIconImage(new ImageIcon("rsc/Pixel-Runner_Icon.png").getImage());

		tarInfos = new JTextArea();
		tarInfos.setBackground(Color.BLACK);
		tarInfos.setForeground(Color.WHITE);
		tarInfos.setFont(new Font("Arial Nova", Font.BOLD | Font.ITALIC, 20));
		tarInfos.setEditable(false);
		tarInfos.setText("~Infos~"
						+ "\n"
						+ "\nPress W, A, S, D, to move the object"
						+ "\nPress UP or DOWN to resize the object"
						+ "\nPress ESCAPE to close the game"
						+ "\n"
						+ "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
		tarInfos.setBounds(10, 11, windowWidth - 30, windowHeight - 50);
		contentPane.add(tarInfos);

	}

}
