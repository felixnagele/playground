/**
 * IPC Channel Names
 * This file has no dependencies and can be safely imported from preload, main, and renderer
 */
export const IPC_CHANNELS = {
  LAUNCH_BROWSER: 'launch-browser',
  CLOSE_BROWSER: 'close-browser',
  BROWSER_STATUS: 'browser-status',
} as const;
