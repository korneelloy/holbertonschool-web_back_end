const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(database)
      .then(({ total, fields }) => {
        const text = `Number of students: ${total}\n`;
        for (const [field] of Object.entries(fields)) {
          console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        }
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`This is the list of our students\n${text}`);
      })
      .catch((error) => {
        console.log(error);
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Cannot load the database');
      });
  }
});

app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;
