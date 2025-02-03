/*
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.
*/

SELECT unique_id, name 
    from Employees 
    left join EmployeeUNI 
    on EmployeeUNI.id = Employees.id