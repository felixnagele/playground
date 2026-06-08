const js = require('@eslint/js');
const tseslint = require('typescript-eslint');
const importPlugin = require('eslint-plugin-import');
const globals = require('globals');
const { FlatCompat } = require('@eslint/eslintrc');

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

module.exports = [
  // GLOBAL IGNORES
  {
    ignores: [
      'eslint.config.*',
      '**/node_modules/**',
      '**/dist/**',
      '**/out/**',
      '**/.vite/**',
      '**/build/**',
      '**/coverage/**',
    ],
  },

  // eslint:recommended
  js.configs.recommended,

  // @typescript-eslint
  tseslint.configs.eslintRecommended,
  ...tseslint.configs.recommended,

  // plugin:import/*
  ...compat.extends('plugin:import/recommended', 'plugin:import/typescript'),

  {
    plugins: {
      import: importPlugin,
    },

    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module',
      globals: {
        ...globals.browser,
        ...globals.node,
      },
    },

    rules: {
      '@typescript-eslint/no-explicit-any': 'off',
    },

    settings: {
      'import/core-modules': ['electron'],
      'import/resolver': {
        typescript: {},
      },
    },
  },
];
