-- Success
-- Details 
-- Runtime: 674 ms, faster than 5.04% of MySQL online submissions for Second Highest Salary.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.

-- SELECT
--   IFNULL(
--     (SELECT DISTINCT Salary
--     FROM Employee
--     ORDER BY Salary DESC
--     LIMIT 1 OFFSET 1), 
--   NULL) AS SecondHighestSalary


Success
Details 
Runtime: 379 ms, faster than 12.86% of MySQL online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.

SELECT (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1) AS SecondHighestSalary;
