SELECT  employee_id , 
        CASE
            WHEN (employee_id % 2 <> 0  and lower(SUBSTRING(name,1,1)) <> 'm' )THEN salary
            ELSE 0
        END AS bonus
FROM    Employees
ORDER BY 1
