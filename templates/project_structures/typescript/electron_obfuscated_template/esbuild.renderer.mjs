import * as esbuild from 'esbuild';

async function buildRenderer() {
  try {
    await esbuild.build({
      entryPoints: ['src/renderer/renderer.ts'],
      bundle: true,
      outfile: 'build/renderer/renderer.js',
      platform: 'browser',
      target: 'esnext',
      format: 'iife',
      sourcemap: true,
      external: [],
      logLevel: 'info',
      minify: false,
    });
    console.log('✓ Renderer bundled successfully');
  } catch (error) {
    console.error('Failed to bundle renderer:', error);
    process.exit(1);
  }
}

buildRenderer();
