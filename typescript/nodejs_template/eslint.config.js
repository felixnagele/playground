// eslint.config.js
import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import securityPlugin from 'eslint-plugin-security';

export default tseslint.config(
  js.configs.recommended,             // ESLint core rules
  tseslint.configs.recommended,       // TypeScript rules
  tseslint.configs.stylistic,         // Style rules (optional)
  {
    plugins: {
      security: securityPlugin,
    },
    rules: {
      // Optional extra rules - extendable
      'no-console': 'warn',
      '@typescript-eslint/no-unused-vars': 'warn',
    },
  }
);
