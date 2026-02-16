import * as os from 'os';
import * as path from 'path';

import type { BrowserContext } from 'playwright';
import { chromium } from 'playwright';

import { DEFAULT_URL } from '../../shared/constants';

export class BrowserManager {
  private context: BrowserContext | null = null;

  async launch(): Promise<void> {
    if (this.context) {
      throw new Error('Browser is already running');
    }

    const userDataDir = path.join(os.homedir(), '.playwright-app-profile');

    this.context = await chromium.launchPersistentContext(userDataDir, {
      headless: false,
      channel: 'chrome',
      viewport: { width: 1280, height: 720 },
    });

    const page = this.context.pages()[0] || (await this.context.newPage());
    await page.goto(DEFAULT_URL);
  }

  async close(): Promise<void> {
    if (!this.context) {
      throw new Error('Browser is not running');
    }

    await this.context.close();
    this.context = null;
  }

  isRunning(): boolean {
    return this.context !== null;
  }
}
