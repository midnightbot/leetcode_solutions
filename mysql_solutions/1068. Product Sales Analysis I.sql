# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales s LEFT JOIN Product p ON
    s.product_id = p.product_id
