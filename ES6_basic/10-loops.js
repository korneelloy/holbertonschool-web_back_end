export default function appendToEachArrayValue(array, appendString) {
  let i = 0;
  for (let idx of array) {
    idx = appendString + idx;
    array[i] = idx;
    i += 1;
  }

  return array;
}
