package io.github.felixnagele.shootergame;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyInput implements KeyListener
{
	public void keyTyped(KeyEvent e) {
	}

	public void keyPressed(KeyEvent e)
	{
		int key = e.getKeyCode();

		if(key == KeyEvent.VK_W) {Var.keys[0] = true;}
		if(key == KeyEvent.VK_A) {Var.keys[1] = true;}
		if(key == KeyEvent.VK_S) {Var.keys[2] = true;}
		if(key == KeyEvent.VK_D) {Var.keys[3] = true;}
	}

	public void keyReleased(KeyEvent e)
	{
		int key = e.getKeyCode();

		if(key == KeyEvent.VK_W) {Var.keys[0] = false;}
		if(key == KeyEvent.VK_A) {Var.keys[1] = false;}
		if(key == KeyEvent.VK_S) {Var.keys[2] = false;}
		if(key == KeyEvent.VK_D) {Var.keys[3] = false;}
	}

}
