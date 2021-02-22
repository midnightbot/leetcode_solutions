# Write your MySQL query statement below
UPDATE Salary
SET sex = case sex
WHEN "m" then "f"
WHEN "f" then "m"
END
WHERE sex in ("m","f")
