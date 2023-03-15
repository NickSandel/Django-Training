# Miniblog

Code repo for Mini blog which is a site built for the assessment module of the course on the Mozilla Developer network:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog

It is part of a repo to store a range of training projects for Django. I have set it up to have a shared virtual environment and a shared requirements file

## Environment Creation

I used virtualenv to create the environment for this project. To create the environment, run the following command (on Windows):
> python -m virtualenv venv
> venv\Scripts\activate

## Installing the requirements
To install the requirements, run the following command:
> pip install -r requirements.txt

## Running the project
This is a django project. To run the project, run the following commands:
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver

## Running the tests
To run the tests with pytest move to the miniblog subfolder and run the following command:
> pytest

For more specific file runs use:
> pytest blog\tests\test_views.py
> pytest blog\tests\test_models.py