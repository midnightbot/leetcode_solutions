# Write your MySQL query statement below
SELECT problem_id
FROM Problems
WHERE likes/(likes+dislikes) < 0.6
order by problem_id
