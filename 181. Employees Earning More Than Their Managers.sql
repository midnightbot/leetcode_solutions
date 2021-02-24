# Write your MySQL query statement below
Select e1.Name as Employee
from Employee e1, Employee e2
where e1.salary > e2.salary and e1.ManagerId = e2.Id
