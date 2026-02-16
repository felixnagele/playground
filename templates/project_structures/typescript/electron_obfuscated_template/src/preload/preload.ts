import { contextBridge, ipcRenderer } from 'electron';

/**
 * IMPORTANT: Channel names must match those in src/shared/ipc-channels.ts
 * Preload scripts cannot import from relative paths without bundling.
 * Tests validate that these string literals match the canonical definitions.
 */

interface BrowserStatus {
  isRunning: boolean;
  message: string;
}

contextBridge.exposeInMainWorld('api', {
  launchBrowser: () => ipcRenderer.invoke('launch-browser'),

  closeBrowser: () => ipcRenderer.invoke('close-browser'),

  onBrowserStatus: (callback: (status: BrowserStatus) => void) => {
    const listener = (_event: unknown, status: BrowserStatus) => {
      callback(status);
    };
    ipcRenderer.on('browser-status', listener);
    return () => {
      ipcRenderer.removeListener('browser-status', listener);
    };
  },
});
