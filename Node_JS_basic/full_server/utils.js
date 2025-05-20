import fs from 'fs';
import csv from 'csv-parser';

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    const fields = {};
    fs.createReadStream(path)
      .on('error', () => reject(new Error('Cannot load the database')))
      .pipe(csv())
      .on('data', (row) => {
        if (!fields[row.field]) {
          fields[row.field] = [];
        }
        fields[row.field].push(row.firstname);
      })
      .on('end', () => {
        const sortedFields = Object.keys(fields).sort().reduce((acc, key) => {
          acc[key] = fields[key];
          return acc;
        }, {});
        resolve(sortedFields);
      });
  });
}

export default readDatabase;
