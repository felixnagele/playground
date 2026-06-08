import { describe, it, expect } from 'vitest';

import { DEFAULT_URL, THEME_STORAGE_KEY } from '../src/shared/constants';
import { IPC_CHANNELS } from '../src/shared/ipc-channels';

describe('Constants', () => {
  it('should have correct IPC channel names', () => {
    expect(IPC_CHANNELS.LAUNCH_BROWSER).toBe('launch-browser');
    expect(IPC_CHANNELS.CLOSE_BROWSER).toBe('close-browser');
    expect(IPC_CHANNELS.BROWSER_STATUS).toBe('browser-status');
  });

  it('should have correct default URL', () => {
    expect(DEFAULT_URL).toContain('https://github.com');
  });

  it('should have correct theme storage key', () => {
    expect(THEME_STORAGE_KEY).toBe('app-theme');
  });
});

describe('Types', () => {
  it('should validate BrowserStatus structure', () => {
    const status: { isRunning: boolean; message: string } = {
      isRunning: true,
      message: 'Browser is running',
    };
    expect(status).toHaveProperty('isRunning');
    expect(status).toHaveProperty('message');
    expect(typeof status.isRunning).toBe('boolean');
    expect(typeof status.message).toBe('string');
  });
});
