export default function getListStudentIds(students) {
  if (!(students instanceof Array)) {
    return ([]);
  }
  const arrayOfId = students.map((student) => student.id);
  return (arrayOfId);
}
