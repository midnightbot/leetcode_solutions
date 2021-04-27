# Write your MySQL query statement below
select a.sale_date, a.sold_num - b.sold_num as diff
from Sales a left join Sales b
on a.sale_date = b.sale_date
where a.fruit = 'apples' and b.fruit = 'oranges'
