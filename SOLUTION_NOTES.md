# Solution Notes

## Initial project setup & dependency installation
### Create the database: 
1. Use the postgres command line utils to create the database - run `createdb chicago_salaries`
2. Log into psql (run `psql`) and then use the psql `\l` command to list all databases and confirm the new database exists. 

### Create the python virtual environment & install dependencies
1. Be sure you are in your project root directory on the command line (it is the same directory where the `README.md` file is).
1. Create a python virtual environment named `.venv`: `python -m venv .venv`
2. Activate your virtual environment: `source .venv/bin/activate`
3. Install psycopg: `pip install psycopg`

### Get the csv file
1. Download the .csv file as instructed in the README and move it into your project root directory

You should now have your project set up so you can start writing code! 