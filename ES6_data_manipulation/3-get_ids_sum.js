export default function getStudentIdsSum(students) {
  if (!(students instanceof Array)) {
    return (0);
  }
  const sum = students.reduce((sum, student) => sum + student.id, 0);
  return (sum);
}
