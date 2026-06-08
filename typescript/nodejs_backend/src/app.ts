import { createServer, type Server } from 'node:http';

export function createApp(): Server {
  return createServer((_req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello World\n');
  });
}
