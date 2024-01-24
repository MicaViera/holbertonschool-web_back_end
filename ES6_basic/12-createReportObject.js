export default function createReportObject(employeesList) {
  const Report = {
    allEmployees: employeesList,
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return Report;
}
