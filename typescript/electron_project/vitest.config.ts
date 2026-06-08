import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['tests/**/*.test.ts', 'tests/**/*.spec.ts'],
    testTimeout: 5_000,
    hookTimeout: 10_000,
    teardownTimeout: 10_000,
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      include: ['src/**/*.ts'],
      exclude: [
        'src/**/*.d.ts',
        'src/main/main.ts',
        'src/preload/preload.ts',
        'src/renderer/renderer.ts',
        'src/renderer/inject.js',
        'src/renderer/**/*.ts', // Renderer UI requires DOM
        'src/main/features/ui/**/*.ts', // UI features require Electron
        'src/main/features/browser/launcher.ts', // Requires Playwright browser context
        'src/main/features/browser/browserSetup.ts', // Requires Playwright setup
      ],
      thresholds: {
        lines: 70,
        functions: 70,
        branches: 70,
        statements: 70,
      },
    },
  },
});
