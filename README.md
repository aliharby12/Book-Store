# Book-Store
this is an online bookstore where the user can view, search and purchase their favorite books.

## General Requirements
* clone the project and go to the project directory using your terminal / CMD
* [Docker](https://docs.docker.com/get-docker/)

## Project Setup
* Copy the content of `.env.template` file and paste into the new created file `.env`
* In `.env` change all configurations to your desired configurations
* Run in you terminal / CMD: `docker build .` (make sure you are in the project directory)
* Run in you terminal / CMD: `docker-compose build` (make sure you are in the project directory)
* Run in you terminal / CMD: `docker-compose up` (make sure you are in the project directory)
* The server should be now running under `http://127.0.0.1:8000/` (if port 8000 is available)
* Admin dashboard is located in `http://127.0.0.1:8000/admin` and the admin credentials are: `admin@admin.com`, `admin@1234`.
* To Run Custom Command, like django shell, just type: `docker-compose run web sh -c "YOUR COMMAND HERE"`.