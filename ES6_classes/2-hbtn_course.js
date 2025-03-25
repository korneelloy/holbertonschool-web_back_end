export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return (this._name);
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw new TypeError('The name must be a string');
    }
    this._name = name;
  }

  get length() {
    return (this._length);
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw new TypeError('The length must be a number');
    }
    this._length = length;
  }

  get students() {
    return (this._students);
  }

  set students(students) {
    if (!(students instanceof Array)) {
      throw new TypeError('The students must be an array');
    }
    for (const student in students) {
      if (typeof student !== 'string') {
        throw new TypeError('A student must be a string');
      }
    }
    this._students = students;
  }
}
