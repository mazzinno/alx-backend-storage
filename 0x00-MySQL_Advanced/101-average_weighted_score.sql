-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all students
-- task 101

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS U, 
    (SELECT U.id, SUM(score * weight) / SUM(weight) AS w_avg 
    FROM users AS U 
    JOIN corrections as C ON U.id=C.user_id 
    JOIN projects AS P ON C.project_id=P.id 
    GROUP BY U.id)
  AS WA
  SET U.average_score = WA.w_avg 
  WHERE U.id=WA.id;
END;
