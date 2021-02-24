# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from Employee
where Salary < (Select max(salary) from Employee)
