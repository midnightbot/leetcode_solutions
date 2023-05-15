# Write your MySQL query statement below
with temp as(
    select followee as person, count(*) as cnt
    from follow
    group by followee
),
temp1 as(
    select follower as person, count(*) as cnt
    from follow
    group by follower
),
temp2 as(
    select t.person, t.cnt as c1, coalesce(t1.cnt,0) as c2
    from temp t left join temp1 t1
    on t.person = t1.person
)

select person as follower, c1 as num
from temp2
where c1>=1 and c2>=1
order by follower asc
