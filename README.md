# News App
Self-created news/blog application with articles, tags, comment sections and filtering posts by categories. The app also features simple API that allows viewing articles and posting comments.

## How to run (using pipenv)
- clone the repository
- start a virtual environment ('pipenv shell')
- pipenv install
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py loaddata db.json
- python3 manage.py runserver

Credentials for testing purposes:<br/>
username: testadmin<br/>
password: admin1441

username: testuser<br/>
password: admin1441

## Stack
- Python, 
- Django, 
- Bootstrap, 
- Django Rest Framework

## I learned
- Class based views, 
- detail view, 
- adding comment section, 
- tags and filtering by tags (using taggit), 
- Django forms,  
- Bootstrap crispy forms,
- custom admin page and filtering, 
- django ORM and managers. 
- DRF generic views for existing models
- DRF implementation of GET and POST methods.
