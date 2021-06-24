-- Success
-- Details 
-- Runtime: 1168 ms, faster than 5.51% of MySQL online submissions for Rank Scores.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.

SELECT 
  Score, 
  (SELECT COUNT(DISTINCT Score) FROM Scores WHERE Score >= s.Score) Rank
FROM
  Scores s
ORDER BY
  Score
DESC;
