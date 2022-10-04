# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets 
WHERE length(TRIM(content)) > 15
