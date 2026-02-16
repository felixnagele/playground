import js from '@eslint/js';
import globals from 'globals';
import tseslint from 'typescript-eslint';
import importPlugin from 'eslint-plugin-import';
import vitest from '@vitest/eslint-plugin';
import { defineConfig } from 'eslint/config';

const tsconfigRootDir = (globalThis as any).process?.cwd?.() ?? '.';

export default defineConfig([
  // --------------------------------------------------
  // Base JS / Node rules
  // --------------------------------------------------
  {
    files: ['**/*.{js,mjs,cjs,ts,mts,cts}'],
    plugins: { js },
    extends: ['js/recommended'],
    languageOptions: { globals: globals.node },
  },

  // --------------------------------------------------
  // TypeScript (syntax + basic semantics, fast)
  // --------------------------------------------------
  tseslint.configs.recommended,

  // --------------------------------------------------
  // Type-aware rules (ONLY for source files)
  // --------------------------------------------------
  {
    files: ['src/**/*.{ts,mts,cts}'],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.json'],
        tsconfigRootDir,
      },
    },
    rules: {
      '@typescript-eslint/no-floating-promises': 'error',
      '@typescript-eslint/no-unsafe-assignment': 'warn',
      '@typescript-eslint/no-unsafe-call': 'warn',
      '@typescript-eslint/no-unsafe-member-access': 'warn',
      '@typescript-eslint/consistent-type-imports': 'warn',
    },
  },

  // --------------------------------------------------
  // Import hygiene (TypeScript-aware)
  // --------------------------------------------------
  {
    plugins: { import: importPlugin },
    settings: {
      'import/parsers': {
        '@typescript-eslint/parser': ['.ts', '.tsx', '.mts', '.cts'],
      },
      'import/resolver': {
        typescript: {
          project: ['./tsconfig.json'],
        },
      },
    },
    rules: {
      'import/no-cycle': 'error',
      'import/no-unused-modules': 'warn',
      'import/order': [
        'warn',
        {
          groups: [
            'builtin',
            'external',
            'internal',
            'parent',
            'sibling',
            'index',
          ],
          'newlines-between': 'always',
        },
      ],
    },
  },

  // --------------------------------------------------
  // Tests (Vitest)
  // --------------------------------------------------
  {
    files: ['tests/**/*.test.ts', '**/*.spec.ts'],
    plugins: { vitest },
    rules: {
      ...(vitest.configs?.recommended?.rules ?? {}),
      'import/no-unused-modules': 'off',
    },
    languageOptions: { globals: vitest.environments?.env?.globals ?? {} },
  },

  // --------------------------------------------------
  // Global ignores
  // --------------------------------------------------
  {
    ignores: [
      'dist/**',
      'build/**',
      'out/**',
      'coverage/**',
      'node_modules/**',
      '*.config.*',
    ],
  },

  // --------------------------------------------------
  // TS ergonomics
  // --------------------------------------------------
  {
    rules: {
      '@typescript-eslint/no-unused-vars': [
        'error',
        { argsIgnorePattern: '^_' },
      ],
      '@typescript-eslint/no-explicit-any': 'warn',
    },
  },
]);
