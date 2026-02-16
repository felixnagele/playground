# Playwright Electron Obfuscated Template

Minimal Electron app with Playwright browser integration and code obfuscation.

## Features

- Launch GitHub in Playwright-controlled Chrome browser
- Light/Dark theme toggle
- TypeScript with full type safety
- Code obfuscation for production builds

## Setup

```bash
npm install
```

## Development

```bash
npm run dev
```

```bash
npm run start
```

## Build & Package

```bash
# Build only
npm run build

# Package for distribution (no installer)
npm run pack

# Create installer
npm run dist
```

## Quality Checks

```bash
# Run all validations
npm run validate

# Run tests
npm test
```

## Dynamic Obfuscation

The obfuscation system **automatically**:

- Discovers all files in your project
- Obfuscates all `.js` files
- Copies all other files (HTML, PNG, SVG, JSON, etc.)
- Excludes: `node_modules/`, `tests/`, build configs

**No manual file list needed!** Add new files/folders and they're automatically included.
