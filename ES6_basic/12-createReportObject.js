export default function createReportObject(employeesList) {
  const reportObject = {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      let i = 0;
      for (const el in employeesList) {
        i += 1;
      }
      return i;
    },
  };
  return reportObject;
}
