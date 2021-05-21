# SMartS - REST API
___________________________
Backend API for managing messages - saving, returning saved, editing and deleting short texts (up to 160 characters).

It supports messages resources including authentication(JWT Token).

- [X] Displaying all messages
- [X] Displaying single message
- [X] Adding new message
- [X] Editing exists message
- [X] Deleting exists message

The application was deployed using the AWS Elastic Beanstalk service.

The documentation can be found in `documentation.html` or [here](https://documenter.getpostman.com/view/15826658/TzXtGfLB#bb0de710-8b0b-4303-bd26-eeba69019dd4).

![documentation](https://github.com/ishabelle/SMartS/blob/main/documentation.jpg?raw=true)

## SETUP
___________________________

- Clone repository
- Create database and user
- Rename .env.example to `.env` and set your parameters:
```angular2html
# SQLALCHEMY_DATABASE_URI MySQL trmplate
SQLALCHEMY_DATABASE_URI = mysql+pymysql://<db_user>:<db_password>@<db_host>/<db_name>?charset=utf8mb4
```
- Create a virtual environment
```angular2html
python -m venv venv
```
- Install packages from `requirements.txt`
```angular2html
pip install -r requirements.txt
```
- Migrate database
```angular2html
flask db upgrade
```
- Run command
```angular2html
flask run
```
### HINT
___________________________
Import / delete exampl data from `smarts\samples`:
```angular2html
# import data
flask db-manage add-data

# remove data
flask db-manage remove-data
```
### TESTS
___________________________
In order to execute test located in `tests/` run the command:
```angular2html
python -m pytest tests/
```