import dotenv from 'dotenv';

import { createApp } from './app.js';

dotenv.config();

const PORT = Number(process.env.PORT) || 3000;

const server = createApp();

server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

const shutdown = (signal: string): void => {
  console.log(`[shutdown] Received ${signal}`);
  server.close(() => process.exit(0));
};

process.once('SIGINT', () => shutdown('SIGINT'));
process.once('SIGTERM', () => shutdown('SIGTERM'));
