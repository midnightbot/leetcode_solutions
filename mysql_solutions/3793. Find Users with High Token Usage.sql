# Write your MySQL query statement below
with temp as(
    select user_id, sum(tokens) as total_tokens, count(*) as prompt_count, max(tokens) as max_tokens
    from prompts
    group by user_id
    having prompt_count >= 3
),
temp1 as (
select user_id, prompt_count, round(total_tokens/prompt_count, 2) as avg_tokens, max_tokens
from temp
having avg_tokens < max_tokens
order by avg_tokens desc, user_id asc
)
select user_id, prompt_count, avg_tokens from temp1
