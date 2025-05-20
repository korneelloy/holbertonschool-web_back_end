import path from 'path';
import readDatabase from '../utils.js';

const db = path.join(__dirname, '../../database.csv');

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase(db)
      .then((fields) => {
        let text = '';
        for (const field in fields) {
          text += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
        }
        res.status(200).type('text').send(`This is the list of our students\n${text}`);
      })
      .catch(() => {
        res.status(500).type('text').send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const major = req.params.major;
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).type('text').send('Major parameter must be CS or SWE');
    }
    readDatabase(db)
      .then((fields) => {
        return res.status(200).type('text').send(`List: ${fields[major].join(', ')}\n`);
      })
      .catch(() => {
        res.status(500).type('text').send('Cannot load the database');
      });
  }
}

export default StudentsController;
