# Write your MySQL query statement below

with temp as (
    select a.user_id, count(distinct(a.session_id)) as cnt
    from Activity a
    where a.activity_date between '2019-06-28' and '2019-07-27'
    group by user_id
)

select coalesce(round(sum(cnt)/count(user_id),2),0) as average_sessions_per_user
from temp
