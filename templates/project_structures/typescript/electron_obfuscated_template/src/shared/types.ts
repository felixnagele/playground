export type Theme = 'light' | 'dark';

export interface BrowserStatus {
  isRunning: boolean;
  message: string;
}

export interface AppAPI {
  launchBrowser: () => Promise<void>;
  closeBrowser: () => Promise<void>;
  onBrowserStatus: (callback: (status: BrowserStatus) => void) => () => void;
}

declare global {
  interface Window {
    api: AppAPI;
  }
}
