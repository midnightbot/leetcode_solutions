select event_day as day, emp_id, sum(out_time) - sum(in_time) as total_time
from Employees 
group by emp_id, event_day
