import type { Browser, Page } from 'playwright';
import { chromium } from 'playwright';

import { DEFAULT_URL } from '../shared/constants';

export class BrowserManager {
  private browser: Browser | null = null;
  private page: Page | null = null;

  async launch(): Promise<void> {
    if (this.browser) {
      throw new Error('Browser is already running');
    }

    console.log('[BrowserManager] Starting browser...');

    try {
      // Try Chrome first, fallback to Chromium
      try {
        console.log('[BrowserManager] Launching Chrome...');
        this.browser = await chromium.launch({
          headless: false,
          channel: 'chrome',
        });
        console.log('[BrowserManager] Chrome launched successfully');
      } catch (chromeError) {
        console.log('[BrowserManager] Chrome failed, trying Chromium...');
        console.error('[BrowserManager] Chrome error:', chromeError);
        this.browser = await chromium.launch({
          headless: false,
        });
        console.log('[BrowserManager] Chromium launched successfully');
      }

      // Create new page
      this.page = await this.browser.newPage();
      console.log('[BrowserManager] Page created');

      // Navigate to URL
      await this.page.goto(DEFAULT_URL, { waitUntil: 'domcontentloaded' });
      console.log('[BrowserManager] Navigated to:', DEFAULT_URL);
    } catch (error) {
      console.error('[BrowserManager] Critical error:', error);
      // Clean up on error
      if (this.browser) {
        await this.browser.close().catch(() => {});
        this.browser = null;
      }
      this.page = null;
      throw error;
    }
  }

  async close(): Promise<void> {
    if (!this.browser) {
      throw new Error('Browser is not running');
    }

    console.log('[BrowserManager] Closing browser...');
    await this.browser.close();
    this.browser = null;
    this.page = null;
    console.log('[BrowserManager] Browser closed');
  }

  isRunning(): boolean {
    return this.browser !== null;
  }
}
