const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');
    let counter = -1;
    const fields = {};
    for (const line of lines) {
      if (counter !== -1 && line !== '') {
        const field = line.split(',')[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(line.split(',')[0]);
      } else if (line === '') {
        counter -= 1;
      }
      counter += 1;
    }
    if (counter === -1) {
      counter = 0;
    }
    console.log(`Number of students: ${counter}`);
    for (const field in fields) {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;