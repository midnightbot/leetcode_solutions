SELECT d.Name AS Department, e.Name AS Employee, e.Salary
FROM Employee AS e, Department AS d
WHERE e.DepartmentId = d.Id AND
e.Salary = (SELECT MAX(Salary) FROM Employee AS t WHERE t.DepartmentId = e.DepartmentId);
