/*
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.
*/
select W1.id from Weather as W1, Weather as W2
where DATEDIFF(W1.recordDate,W2.recordDate) = 1
and W1.temperature > W2.temperature

--DATEDIFF() Allows you to be able to calculate the difference between different datetime types

-- Big takeaway here is querying the data twice then comparing...