# Your code goes here!
import psycopg

connection = psycopg.connect("dbname=chicago_salaries")


"""
Find the employee being paid the most
    - hourly
        SELECT  (employees.hourly_rate * employees.typical_hours) -- have to calculate rate * hours
        FROM employees
        WHERE employment_type='hourly'
    - salaried
        SELECT annual_salary from EMPLOYEES 
        WHERE employment_type='salary'
        ORDER BY annual_salary DESCENDING
        LIMIT 1;

        or use greatest() ? 

Find the employee being paid the least
    - not hard once we find being paid the most, just reverse ordering

Find the department with the highest average salary
    1. get all departments
        SELECT department from EMPLOYEES GROUP BY department

    2. calculate salary for each department
        - Run a separate query for each department
            - hourly or annual or both? Run a separate query for each
                - start with annual

Find the department with the lowest average salary
    - not hard once we find highest average salary

Find the average salary difference between full time and part time workers
    1. Get average salary of all full time (salaried) workers
    2. Get average salary of all part time (hourly) workers
    3. Subtract to get the difference
Find the most common first name
SELECT first_name, COUNT(first_name) as num_employees_with_name
ORDER BY num_employees_with_name DESCENDING

Find the most common last name
    - not hard once we find the most common first name

If there are people with the same name, find what their job titles, departments, and annual salaries are
"""
