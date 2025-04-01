export default function cleanSet(theSet, startString) {
  let theString = '';
  let updatedElement = '';
  if (startString === '') {
    return theString;
  }
  for (const element of theSet) {
    if (element.indexOf(startString) === 0) {
      if (theString === '') {
        updatedElement = element.replace(startString, '');
      } else {
        updatedElement = element.replace(startString, '-');
      }
      theString += updatedElement;
    }
  }
  return theString;
}
