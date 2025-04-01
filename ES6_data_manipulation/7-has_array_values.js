export default function hasValuesFromArray(theSet, theArray) {
  for (const element of theArray) {
    if (!(theSet.has(element))) {
      return false;
    }
  }
  return true;
}
