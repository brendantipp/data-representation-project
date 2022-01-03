# Brendan Ryan Data Representation Project December 2021

## Project Description 

Write a program that demonstrates an understand of  creating and consuming RESTful APIs

I decided to create a tasks web application which 

1. Allows me to add/create tasks
2. Update and edit these tasks
3. Delete a task

The application also links to the Google Gmail API which extracts emails sent to brendanstasks@gmail.com

The user also has the ability to extract the emails using the google Gmail API and save as a csv file

## Folder structure 

## SQL fodler

This folder contains the database backup of two tables:

1. The projectdb_todo.sql file which is the backup of the tasks table in MySQL
2. The projectdb_users.sql file which is the back up the users table in MySQL

## Templates folder

- This containts the tempalte hmtl pages index.html, login.html and task.html

Other files
- a Message.json is the json extract from the gmail api
- emails.csv is the csv extract from the google gmail API


#### HMTL files
- gmailapi.html is the page which shows the extracted gmail tasks using the API
- task.html is the page which shows a listing of my tasks and gives links to update create and delete tasks
- project.html - gives an overview of the project 

#### Python files

- messages.py is the python file with teh code to connect to and extract the messages for the API
- server.py - is my flash app server restful API, performs my CRUD operations
- todoDAO.py - contains my python functions , deals with msqlconnector, convert formats

## Contact

I can be contacted at 

