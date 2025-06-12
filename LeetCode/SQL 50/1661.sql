/*

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
The table shows the user activities for a factory website.
(machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
machine_id is the ID of a machine.
process_id is the ID of a process running on the machine with ID machine_id.
activity_type is an ENUM (category) of type ('start', 'end').
timestamp is a float representing the current time in seconds.
'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
It is guaranteed that each (machine_id, process_id) pair has a 'start' and 'end' timestamp.

*/

SELECT A1.machine_id, ROUND(AVG(A2.timestamp - a1.timestamp),3) 
AS    processing_time
FROM  Activity A1, Activity A2
WHERE A1.machine_id = A2.machine_id
AND   A1.process_id = A2.process_id
AND   A1.activity_type = 'start'
AND   A2.activity_type = 'end'
GROUP BY A1.machine_id