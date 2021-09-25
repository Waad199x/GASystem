
## Introduction

# Project Idea :
To help arranging Online chat groups for reciting qura'an (it can be used on any kind of groups arrangement needs)
having 3 different types of roles increases the authentication and make the arrangement process better 


# Project motivation 
Personally I have been always thinking about a way to simplify the group arrangement process for any need. In my case, once I was a supervisor in a Qura'an recitation program and I suffered a lot arranging those "what's up" groups, keeping a record of the contact info for hundreds of students and teachers wasn't easy. So, In this project you can see the beginning of a big system that will simplify the arrangement process to be done much easier! InshaAllah. 


## Project Details:
# Type of Roles

`Teachers role`
   - Can get the groups information only.
   - For each group they can view the students list info 

`Supervisor role`
Can do the following :
   - view the information of the groups 
   - Edit,add,delete the group information (teachers+students info) 

`Manager role`
Can do the following :
   - Everything the other roles do 
   - Edit, create, delete a whole group not only the infos  



## Project Structure

  ```sh

  ├── MILSONE
  |   ├── Project README
  |   ├── frontend
  |   |   └── src
  |   |      ├── app ** "Almost all the frontend pages"
  |   |      └── environment ** "Has 2 files with Auth0 settings"
  |   └── backend
  |      ├── src
  |      |   ├── api.py ** "The main driver of the app."
  |      |   ├── auth 
  |      |   |   └── auth.py ** "Main file for implementing Authuntication process"
  |      |   └── database 
  |      |       ├── database2.db ** "database for the app"
  |      |       └── models.py ** "implemetaion of the database tables and so on"
  |      ├── Groups arrangment project ** "POSTMAN tests"
  |      ├── requirements ** "Dependencies"
  |      └── Unittests
        
  ```


# Needed Dependencies
If you want to check the dependencies needed to run this project
before installing go to the following path (./backend/requirements.txt)



## Steps To Run The Project 

Project running commands are divided into 2 sections :

1.  requirements configuration ( run once )
`Creating a virtual environment with the required dependencies installed using requirments.txt`

```sh
    cd # Write the directory path where you saved the project

    virtualenv myownenv # place any name for the virtual environment

    myownenv\Scripts\activate # replace 'myownenv' with the name you wrote in the past step

    cd backend 

    pip install -r requirements.txt # to install all the required dependencies 
```

2. turn on the server (run every time)`
`runs the project from the virtual environment made before`

```sh
    cd # Write the directory path where you saved the project

    myownenv\Scripts\activate # replace 'myownenv' with the name of your own vir. env.

    cd backend\src

    set FLASK_APP=api.py

    set FLASK_ENV=development

    flask run --reload

```
## Steps To Run The Project Frontend

```sh
    cd # Write the directory path where you saved the project

    myownenv\Scripts\activate # replace 'myownenv' with the name of your own vir. env.
    
    npm install

    cd frontend

    npm start

    URL : http://localhost:4200/
```
## Testing 

There are 2 different ways for testing the endpoints 

1. Using POSTman:
`it tests all the methods(GET, POST, PATCH, DELETE) with the right code respond `
`You can import the POSTman collection from the following path (./backend/Groups arrangment project.postman_collection.json)`

2. Using Unittest: : 
`There are 2 tests for each endpoint (total 10 tests) one with successful request and the other with failed request`
`check the unittest by opening your terminal and navigate to the backend directory and turn on you vir. inv. by the following commands :`
```sh
    cd # go to the directory path where you saved the project

    myownenv\Scripts\activate # replace 'myownenv' with the name of your own vir. env.

    cd backend

    python -m unittest Unittests

```

##The Application is hosted on 
## https://ga-system.herokuapp.com/

