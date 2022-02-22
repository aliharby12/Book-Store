# Book-Store
this is an online bookstore where the user can view, search and purchase their favorite books.

## General Requirements
* clone the project and go to the project directory using your terminal / CMD
* [Python](https://www.python.org/downloads/) 3.9 or above (if you are using mac or linux, you have to make sure that your default python version is 3.9 or above)
* [Install Docker](https://docs.docker.com/get-docker/)

## Project Setup
* Copy the content of `.env.template` file and paste into the new created file `.env`
* In `.env` change all configurations to your desired configurations
* Run in you terminal / CMD: `docker build .` (make sure you are in the project directory)
* Run in you terminal / CMD: `docker-compose build` (make sure you are in the project directory)
* Run in you terminal / CMD: `docker-compose up` (make sure you are in the project directory)
* The server should be now running under `http://127.0.0.1:8000/` (if port 8000 is available)
* Migrate your database: `docker-compose run web python manage.py migrate`
* Create a superuser to access the dashboard: `docker-compose run web python manage.py createsuperuser`
* Admin dashboard is located in `http://127.0.0.1:8000/admin`

