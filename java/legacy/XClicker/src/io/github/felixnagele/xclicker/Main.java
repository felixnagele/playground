package io.github.felixnagele.xclicker;

import java.awt.EventQueue;
import java.awt.Toolkit;
import java.math.BigInteger;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextField;
import java.awt.Color;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.awt.event.ActionEvent;
import javax.swing.SwingConstants;
import javax.swing.JCheckBox;

public class Main extends JFrame
{

	private JPanel contentPane;
	private JLabel lblVersion;
	private JLabel lblCreator;
	private JLabel lblTitle;
	private JLabel lblScore;
	private JButton btnClicker;
	private JTextField txtScore;
	private JLabel lblShop;
	private JLabel lblBonus2;
	private JLabel lblBonus3;
	private JLabel lblBonus4;
	private JLabel lblBonus5;
	private JLabel lblBonus6;
	private JCheckBox chckbxNewCheckBox;
	private JCheckBox chckbxNewCheckBox_1;
	private JCheckBox chckbxNewCheckBox_2;
	private JCheckBox chckbxNewCheckBox_3;
	private JCheckBox chckbxNewCheckBox_4;
	private int multiplier = 1;
	private int upgradeLevel = 0;
	private BigInteger score = BigInteger.ZERO;
	private JButton btnUpgrade;
	private JLabel lblMultiplier;

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
					Main frame = new Main();
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
	public Main()
	{
		initComponents();
	}
	private void initComponents() {
		int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
		int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;
		int windowSize = Math.min(screenWidth, screenHeight) * 3 / 4;

		setTitle("X-Clicker");
		setResizable(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, windowSize, windowSize);
		contentPane = new JPanel();
		contentPane.setForeground(Color.BLACK);
		contentPane.setBackground(Color.BLACK);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		setIconImage(loadImage("rsc/X-Clicker_Icon.png"));

		lblTitle = new JLabel("X-CLICKER");
		lblTitle.setForeground(Color.WHITE);
		lblTitle.setFont(new Font("Berlin Sans FB Demi", Font.PLAIN, 50));
		contentPane.add(lblTitle);

		lblVersion = new JLabel("Version 0.0");
		lblVersion.setForeground(Color.WHITE);
		contentPane.add(lblVersion);

		lblCreator = new JLabel("Made by FeliixZ");
		lblCreator.setForeground(Color.WHITE);
		contentPane.add(lblCreator);

		lblScore = new JLabel("X-Score");
		lblScore.setFont(new Font("Arial", Font.PLAIN, 25));
		lblScore.setForeground(Color.WHITE);
		contentPane.add(lblScore);

		lblMultiplier = new JLabel("x1");
		lblMultiplier.setFont(new Font("Arial", Font.PLAIN, 25));
		lblMultiplier.setForeground(Color.GREEN);
		contentPane.add(lblMultiplier);

		btnClicker = new JButton("");
		btnClicker.setForeground(Color.BLACK);
		btnClicker.setBackground(Color.BLACK);
		ImageIcon ico = new ImageIcon(loadImage("rsc/btnScore.png"));
		btnClicker.setIcon(ico);
		btnClicker.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				btnClickerActionPerformed(arg0);
			}
		});
		contentPane.add(btnClicker);

		txtScore = new JTextField();
		txtScore.setHorizontalAlignment(SwingConstants.RIGHT);
		txtScore.setFont(new Font("Arial", Font.PLAIN, 20));
		txtScore.setEditable(false);
		txtScore.setText("0");
		txtScore.setForeground(Color.BLACK);
		contentPane.add(txtScore);
		txtScore.setColumns(10);

		lblShop = new JLabel("Shop");
		lblShop.setForeground(Color.WHITE);
		lblShop.setFont(new Font("Arial", Font.PLAIN, 20));
		contentPane.add(lblShop);

		btnUpgrade = new JButton("Upgrade x2 (100)");
		btnUpgrade.setFont(new Font("Arial", Font.PLAIN, 14));
		btnUpgrade.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				upgradeMultiplier();
			}
		});
		contentPane.add(btnUpgrade);

		positionComponents();

		this.addComponentListener(new ComponentAdapter() {
			public void componentResized(ComponentEvent e) {
				positionComponents();
			}
		});
	}

	private void positionComponents() {
		int windowWidth = contentPane.getWidth();
		int windowHeight = contentPane.getHeight();
		int centerX = windowWidth / 2;

		lblTitle.setBounds(centerX - 125, 37, 250, 58);
		lblVersion.setBounds(windowWidth - 77, windowHeight - 54, 71, 14);
		lblCreator.setBounds(10, windowHeight - 54, 92, 14);
		lblScore.setBounds(centerX - 300, 165, 132, 34);
		lblMultiplier.setBounds(centerX + 180, 165, 100, 34);
		txtScore.setBounds(centerX - 150, 165, 279, 34);
		btnClicker.setBounds(centerX - 125, 250, 250, 250);
		lblShop.setBounds(centerX - 200, windowHeight - 200, 100, 25);
		btnUpgrade.setBounds(centerX - 200, windowHeight - 170, 150, 40);
	}
	protected void btnClickerActionPerformed(ActionEvent arg0)
	{
		score = score.add(BigInteger.valueOf(multiplier));
		this.txtScore.setText(score.toString());
	}

	private BigInteger getUpgradeCost()
	{
		if(upgradeLevel == 0) return BigInteger.valueOf(100);
		double baseCost = 100.0;
		for(int i = 0; i < upgradeLevel; i++)
		{
			baseCost = baseCost * 1.5;
		}
		return BigInteger.valueOf((long)baseCost);
	}

	private void upgradeMultiplier()
	{
		BigInteger cost = getUpgradeCost();

		if(score.compareTo(cost) >= 0)
		{
			score = score.subtract(cost);
			upgradeLevel++;
			multiplier = upgradeLevel + 1;
			this.txtScore.setText(score.toString());
			this.lblMultiplier.setText("x" + multiplier);

			BigInteger nextCost = getUpgradeCost();
			this.btnUpgrade.setText("Upgrade x" + (multiplier + 1) + " (" + nextCost.toString() + ")");
		}
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
