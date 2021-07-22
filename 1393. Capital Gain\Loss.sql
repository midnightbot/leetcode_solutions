# Write your MySQL query statement below
SELECT stock_name, sum(if(operation = 'Buy', -price, price)) as capital_gain_loss
FROM Stocks
GROUP BY stock_name;
