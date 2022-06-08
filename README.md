# Galleria


#### By Joylene Kirui

# Description
Gallery is a photo gallery web application to showcase beautiful pictures. Users get can view photos uploaded by admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories.

# Features
- The home page allows users to see various images.
- User can see all images per location they were taken.
- Users can also search for images based categories.
- Admin can upload images from a django dashboard.

# Live link
Lhttps://myfavoritegallery.herokuapp.com/

# Requirements
The Galleria project requires a prerequisite understanding of the following:

- Django Framework

- Python3.8

- Postgres

- Python virtualenv

# Setup and Installation
##### Clone repo (git clone https://github.com/JoyleneKirui/Gallery.git)

####  Create and Activate virtual environment
-python3 -m venv virtual

-source virtual/bin/activate

#### Install dependancies
Install dependancies that will create an environment for the app to run pip install -r requirements.txt

#### Create the Database
- psql

- CREATE DATABASE mygallery;

#### Run initial Migration
python3 manage.py makemigrations gallery

python3 manage.py migrate

#### Run the app
python3 manage.py runserver

Open terminal on localhost:8000

## Known bugs
No known bugs so far.

## Technologies Used
- Python 3.8

- Django MVC framework

- HTML, CSS and Bootstrap

- JavaScript

- Postgressql

- Heroku

##  License
Copyright (c) [2022] [Joylene Kirui]
[MIT License](https://choosealicense.com/licenses/mit/)