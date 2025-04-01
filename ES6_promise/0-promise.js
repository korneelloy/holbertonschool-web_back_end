export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    if (true) {
      resolve('ok');
    } else {
      reject(Error);
    }
  });
}
