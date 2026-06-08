# Electron Vite Template

This project is built with **Electron + Typescript + Vite**.

## Setup

Install dependencies:

```bash
npm install
```

## Caution

DO NOT run the following command after installing dependencies, as it may break the setup, it says:

To address all issues (including breaking changes), run:

```bash
npm audit fix --force
```

It's important that all @electron-forge packages remain on the exact same version to avoid compatibility issues!!!

## Development

Run in development mode

```bash
npm run start
```

## Production

Build package for production

```bash
npm run package
```

Build distributable installers

```bash
npm run make
```

Publish release

```bash
npm run publish
```

## Validate

Validate Project

```bash
npm run validate
```

## Testing

Run tests:

```bash
npm test
```

## Project Structure

- `src/` - TypeScript source code
- `out/` - Electron Forge output
- `.vite/` - Vite build files
- `tests/` - Test files
- Various config files for ESLint, Prettier, TypeScript and other tools
