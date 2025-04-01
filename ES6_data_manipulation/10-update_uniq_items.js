export default function updateUniqueItems(groceriesMap) {
  for (const [key, value] of groceriesMap) {
    if (value === 1) {
      groceriesMap.set(key, 100);
    }
  }
  return groceriesMap;
}
