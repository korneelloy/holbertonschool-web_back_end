const http = require('http');

const app = http.createServer((req, res) => {
  res.end('Hello Holberton School!');
});

app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;
