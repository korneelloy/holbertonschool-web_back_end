export default class Airport {
  constructor(name, code){
    this.name = name;
    this.code = code;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name should be a string');
    }
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code !== 'string') {
      throw new TypeError('Code should be a string');
    }
    this._code = code;
  }

  toString() {
    return (`[object ${this.code}]`);
  }
}
