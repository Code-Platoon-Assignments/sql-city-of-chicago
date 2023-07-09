# City of Chicago Challenge
In this challenge, we are going to grab a live data set from the City of Chicago, parse through the columns, clean the data as it comes in, and insert it into the database. After that, we'll query the database and find some important data points.

## Release 0: Get the dataset
Visit [the data portal](https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/xzkq-xp2w) and download the CSV (Export Button -> CSV). There should be a pretty significant number of rows!

## Release 1: Create a database
Create a database on your computer called `chicago_salaries` using the command `createdb`. Install the Python library `psycopg` and use it to connect to the database you just created and create an `employees` table with the following columns:
  - first_name
  - last_name
  - job_title
  - full_or_part_time
  - department
  - annual_salary

> **Note**: If an employee is an hourly employee, calculate their `annual_salary` by the equation: `hours_per_week * hourly_salary * 50` (50 work weeks in a year)

For this release, assume all datatypes are varchar(255), just see if you can get the data in the database.

## Release 2: Clean/insert the data 
In this release, do the same as above, but as you iterate over each row, clean the data, and insert the cleaned record into the database. That means you are going to want to update the table's schema to match the new datatypes. Note the calculation for the annual salary we mentioned above.

> Keep an eye out for two things:
> 1) We want first name and last name split in our database but the City of Chicago just has one name field. You will need to split these up from the csv as part of sanitizing the data.
> - 2) everything read in our CSV will be a string by default - how can you convert a string representing a number to an number number in Python?

## Release 3: Queries
Now that we have a database full of employees and their salaries, let's write some query against our database:

1. Find the employee being paid the most
2. Find the employee being paid the least
3. Find the department with the highest average salary
4. Find the department with the lowest average salary
5. Find the average salary difference between full time and part time workers
6. Find the most common first name
7. Find the most common last name
8. If there are people with the same name, find what their job titles, departments, and annual salaries are

## Resources
For some of these queries you will benefit from using the [aggregate functions](https://www.postgresqltutorial.com/postgresql-aggregate-functions/) built into Postgres, specifically [AVG](https://www.postgresqltutorial.com/postgresql-aggregate-functions/postgresql-avg-function/)
