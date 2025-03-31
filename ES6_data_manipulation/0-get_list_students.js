//  function that returns an array of objects
export default function getListStudents() {
  // define student object
  function Student(id, firstName, location) {
    this.id = id;
    this.firstName = firstName;
    this.location = location;
  }

  // create instances of student objects
  const guillaume = new Student(1, 'Guillaume', 'San Francisco');
  const james = new Student(2, 'James', 'Columbia');
  const serena = new Student(5, 'Serena', 'San Francisco');

  // create list fo students:
  const listStudents = [guillaume, james, serena];
  return (listStudents);
}
