export default function getStudentsByLocation(students, city) {
  if (!(students instanceof Array)) {
    return ([]);
  }
  const arrayOfStudentsInCity = students.filter((student) => student.location === city);
  return (arrayOfStudentsInCity);
}
