const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n');

    const fields = {};
    const students = lines.slice(1);

    for (const line of students) {
      if (line.trim() === '') continue;

      const parts = line.split(',');

      const name = parts[0];
      const field = parts[3];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(name);
    }

    console.log(`Number of students: ${students.length}`);
    for (const field in fields) {
      console.log(
        `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
