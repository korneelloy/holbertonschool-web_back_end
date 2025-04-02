export default function updateStudentGradeByCity(students, city, newGrades) {
  if (!(students instanceof Array) || !(newGrades instanceof Array)) {
    return ([]);
  }

  const newArray = students
    .filter((student) => student.location === city)
    .map((student) => {
      const newGrade = newGrades.find((newGrade) => newGrade.studentId === student.id);
      let grades = 'N/A';
      if (newGrade !== undefined) {
        grades = newGrade.grade;
      }
      return {
        ...student,
        grade: grades,
      };
    });
  return newArray;
}
