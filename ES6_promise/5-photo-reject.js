export default function uploadPhoto(filename) {
  const promise = Promise.reject(Error(`${filename} cannot be processed`));
  return promise;
}
