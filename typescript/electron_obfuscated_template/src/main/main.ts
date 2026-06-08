import * as path from 'path';

import { app, BrowserWindow, ipcMain } from 'electron';

import { IPC_CHANNELS } from '../shared/ipc-channels';
import type { BrowserStatus } from '../shared/types';
import { BrowserManager } from '../renderer/ui/browser';

let mainWindow: BrowserWindow | null = null;
const browserManager = new BrowserManager();

function createWindow(): void {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, '../preload/preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
    },
  });

  void mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'));

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

function sendBrowserStatus(status: BrowserStatus): void {
  if (mainWindow) {
    mainWindow.webContents.send(IPC_CHANNELS.BROWSER_STATUS, status);
  }
}

ipcMain.handle(IPC_CHANNELS.LAUNCH_BROWSER, async () => {
  try {
    console.log('[Main] Launching browser...');
    await browserManager.launch();
    console.log('[Main] Browser launched successfully');
    sendBrowserStatus({ isRunning: true, message: 'Browser is running' });
  } catch (error) {
    console.error('[Main] Launch error:', error);
    const errorMessage =
      error instanceof Error ? error.message : 'Unknown error';
    sendBrowserStatus({ isRunning: false, message: `Error: ${errorMessage}` });
  }
});

ipcMain.handle(IPC_CHANNELS.CLOSE_BROWSER, async () => {
  try {
    console.log('[Main] Closing browser...');
    await browserManager.close();
    console.log('[Main] Browser closed successfully');
    sendBrowserStatus({ isRunning: false, message: 'Browser closed' });
  } catch (error) {
    console.error('[Main] Close error:', error);
    const errorMessage =
      error instanceof Error ? error.message : 'Unknown error';
    sendBrowserStatus({
      isRunning: browserManager.isRunning(),
      message: `Error: ${errorMessage}`,
    });
  }
});

void app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', async () => {
  if (browserManager.isRunning()) {
    await browserManager.close();
  }
});
