package io.github.felixnagele.pixelrunner;
import java.awt.EventQueue;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.UIManager;
import java.awt.Color;
import java.awt.Font;
import javax.swing.SwingConstants;

public class FrmMain extends JFrame
{

	private JPanel contentPane;
	private JLabel lblTitle;
	private JButton btnStart;
	private JButton btnCredits;
	private JButton btnExit;
	private JButton btnInfos;

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
					FrmMain frame = new FrmMain();
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
	public FrmMain()
	{
		initComponents();
	}
	private void initComponents() {
		int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
		int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;
		int windowWidth = screenWidth / 4;
		int windowHeight = screenHeight / 2;

		setTitle("Pixel-Runner");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, windowWidth, windowHeight);
		contentPane = new JPanel();
		contentPane.setBackground(Color.BLACK);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		setIconImage(new ImageIcon("rsc/Pixel-Runner_Icon.png").getImage());

		int buttonWidth = 125;
		int buttonHeight = 23;
		int centerX = windowWidth / 2 - buttonWidth / 2;

		lblTitle = new JLabel("Pixel-Runner");
		lblTitle.setHorizontalAlignment(SwingConstants.CENTER);
		lblTitle.setFont(new Font("Arial Nova", Font.BOLD | Font.ITALIC, 20));
		lblTitle.setForeground(Color.WHITE);
		lblTitle.setBounds(centerX, windowHeight / 8, buttonWidth, 31);
		contentPane.add(lblTitle);

		btnStart = new JButton("Start Game");
		btnStart.setFont(new Font("Arial Nova", Font.BOLD | Font.ITALIC, 15));
		btnStart.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				btnStartActionPerformed(arg0);
			}
		});
		btnStart.setBounds(centerX, windowHeight / 8 + 80, buttonWidth, buttonHeight);
		contentPane.add(btnStart);

		btnCredits = new JButton("Credits");
		btnCredits.setFont(new Font("Arial Nova", Font.BOLD | Font.ITALIC, 15));
		btnCredits.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				btnCreditsActionPerformed(e);
			}
		});
		btnCredits.setBounds(centerX, windowHeight / 8 + 124, buttonWidth, buttonHeight);
		contentPane.add(btnCredits);

		btnInfos = new JButton("Infos");
		btnInfos.setFont(new Font("Arial Nova", Font.BOLD | Font.ITALIC, 15));
		btnInfos.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				btnInfosActionPerformed(e);
			}
		});
		btnInfos.setBounds(centerX, windowHeight / 8 + 168, buttonWidth, buttonHeight);
		contentPane.add(btnInfos);

		btnExit = new JButton("Exit");
		btnExit.setFont(new Font("Arial Nova", Font.BOLD | Font.ITALIC, 15));
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				btnExitActionPerformed(e);
			}
		});
		btnExit.setBounds(centerX, windowHeight / 8 + 213, buttonWidth, buttonHeight);
		contentPane.add(btnExit);
	}
	protected void btnStartActionPerformed(ActionEvent arg0)
	{
		FrmGame frame = new FrmGame();
		frame.setVisible(true);
	}
	protected void btnCreditsActionPerformed(ActionEvent e)
	{
		FrmCredits frame = new FrmCredits();
		frame.setVisible(true);
	}
	protected void btnInfosActionPerformed(ActionEvent e)
	{
		FrmInfos frame = new FrmInfos();
		frame.setVisible(true);
	}
	protected void btnExitActionPerformed(ActionEvent e)
	{
		System.exit(0);
	}

}
