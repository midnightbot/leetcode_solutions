# Write your MySQL query statement below
select s1.gender, s1.day, sum(s2.score_points) as total
from Scores as s1 join Scores as s2 on s1.gender = s2.gender and s1.day >= s2.day
group by s1.gender, s1.day
order by gender, day;
