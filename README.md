# SMartS - REST API
Backend API for managing messages - saving, returning saved, editing and deleting short texts (up to 160 characters).

It supports messages resources including authentication(JWT Token).

- [X] Displaying all messages
- [X] Displaying single message
- [X] Adding new message
- [X] Editing exists message
- [X] Deleting exists message

The application was deployed using the AWS Elastic Beanstalk service.

The documentation can be found in `documentation.html` or [here](https://documenter.getpostman.com/view/15826658/TzXtGfLB#bb0de710-8b0b-4303-bd26-eeba69019dd4?raw=true) - with methods and URLs.

![documentation](https://github.com/ishabelle/SMartS/blob/main/info-files/documentation.JPG?raw=true)

## SETUP

- Clone repository
- Create database and user
- Rename .env.example to `.env` and set unique parameters:
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
Import / delete exampl data from `smarts\samples`:
```angular2html
# import data
flask db-manage add-data

# remove data
flask db-manage remove-data
```
### TESTS
In order to execute test located in `tests/` run the command:
```angular2html
python -m pytest tests/
```
### TECHNOLOGIES / TOOLS
| Python 3.9.5 | Flask 2.0.0 | Alembic 1.6.2 |
|:---:|:---:|:---:|
| SQLAlchemy 1.4.15 | PyJWT 1.7.1 | Pytest 6.2.4 |
|MySQL| AWS| Postman|
