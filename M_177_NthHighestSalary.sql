-- Success
-- Details 
-- Runtime: 522 ms, faster than 19.27% of MySQL online submissions for Nth Highest Salary.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Nth Highest Salary.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET M
  );
END