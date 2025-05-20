import http from 'http';
import app from './routes/index.js';

const port = 1245;
const server = http.createServer(app);

server.listen(port);

export default app;
