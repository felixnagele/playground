package io.github.felixnagele.dotlines;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.Color;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JFileChooser;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.io.FileWriter;

public class LineFrame extends JFrame {

	private JPanel contentPane;
	private LinePanel linePanel;
	private Line line = new Line();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					LineFrame frame = new LineFrame();
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
	public LineFrame() {
		initComponents();
	}
	private void initComponents() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 829, 504);

		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);

		JMenu mnFile = new JMenu("File");
		menuBar.add(mnFile);

		JMenuItem mntmOpen = new JMenuItem("Open...");
		mntmOpen.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser fc = new JFileChooser();
				fc.setCurrentDirectory(new File("IOData"));
				int result = fc.showOpenDialog(LineFrame.this);
				if(result == JFileChooser.APPROVE_OPTION)
				{
					File file = fc.getSelectedFile();
					try
					{
						BufferedReader br = new BufferedReader(new FileReader(file));
						line.clear();
						String line_str;
						while((line_str = br.readLine()) != null)
						{
							String[] coords = line_str.split(";");
							for(int i = 0; i < coords.length; i += 2)
							{
								if(i + 1 < coords.length)
								{
									Dot dot = new Dot();
									dot.setX(Integer.parseInt(coords[i]));
									dot.setY(Integer.parseInt(coords[i+1]));
									line.addDot(dot);
								}
							}
						}
						br.close();
						linePanel.repaint();
					}
					catch(Exception ex)
					{
						ex.printStackTrace();
					}
				}
			}
		});
		mnFile.add(mntmOpen);

		JMenuItem mntmSave = new JMenuItem("Save...");
		mntmSave.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser fc = new JFileChooser();
				fc.setCurrentDirectory(new File("IOData"));
				int result = fc.showSaveDialog(LineFrame.this);
				if(result == JFileChooser.APPROVE_OPTION)
				{
					File file = fc.getSelectedFile();
					try
					{
						BufferedWriter bw = new BufferedWriter(new FileWriter(file));
						String lineStr = line.toString();
						if(lineStr.endsWith(";"))
						{
							lineStr = lineStr.substring(0, lineStr.length()-1);
						}
						bw.write(lineStr);
						bw.close();
					}
					catch(Exception ex)
					{
						ex.printStackTrace();
					}
				}
			}
		});
		mnFile.add(mntmSave);

		JMenuItem mntmClear = new JMenuItem("Clear");
		mntmClear.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e)
			{
				line.clear();
				linePanel.repaint();
			}
		});
		mnFile.add(mntmClear);

		JMenuItem mntmExit = new JMenuItem("Exit");
		mntmExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e)
			{
				System.exit(0);
			}
		});
		mnFile.add(mntmExit);
		contentPane = new JPanel();
		contentPane.setBackground(Color.WHITE);
		contentPane.setBorder(new EmptyBorder(0, 0, 0, 0));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);

		linePanel = new LinePanel(line);
		linePanel.setBackground(Color.DARK_GRAY);
		contentPane.add(linePanel, BorderLayout.CENTER);
	}

}
