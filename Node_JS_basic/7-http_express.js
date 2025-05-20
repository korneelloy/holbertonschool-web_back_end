const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents('database.csv')
    .then(({ total, fields }) => {
      let text = `Number of students: ${total}\n`;
      for (const field in fields) {
        text += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      }
      res.status(200).type('text').send(`This is the list of our students\n${text}`);
    })
    .catch(() => {
      res.status(500).type('text').send('Cannot load the database');
    });
});

app.listen(1245, () => {
  console.log('Express server running on port 1245');
});

module.exports = app;
