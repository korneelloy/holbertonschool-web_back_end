export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(`${error.name}: ${error.message}`);
  }
  queue.push('Guardrail was processed');
  return (queue);
}
