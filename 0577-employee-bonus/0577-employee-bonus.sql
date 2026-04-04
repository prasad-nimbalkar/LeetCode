SELECT name, bonus
FROM Employee E
LEFT JOIN Bonus B on B.empId = E.empId
WHERE bonus < 1000 or bonus is NULL