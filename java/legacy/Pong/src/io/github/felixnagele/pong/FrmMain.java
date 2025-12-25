package io.github.felixnagele.pong;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class FrmMain extends javax.swing.JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrmMain frame = new FrmMain();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public FrmMain() {
		setDefaultCloseOperation(FrmMain.EXIT_ON_CLOSE);
		setBounds(0, 0, 500, 350);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(0, 0, 0, 0));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
		this.setLocationRelativeTo(null);
		this.setResizable(false);

		PnlGame pnlGame = new PnlGame();
		contentPane.add(pnlGame, BorderLayout.CENTER);

	}

}
