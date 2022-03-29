
# Django Project

This project is implementation for the following topics related to technologies used with Django

-Implemented Complete Auth Using Custom Auth Model.
    
1. Used built in AbstractBaseUser as parent Auth Model
2. Build Custom Manager for the same
3. Implemented custom error View for customizing Templates
4. Login. SingUp, Logout, Account Views Implemented
5. In built views of PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView
6. Build Custom Templates for These Inbuilt Views
7. Reset Password is working 
8. If kyc is False then it will show you Get Kyc Details unless it will welcome you. By default every user is non kycied.
9. If you want to kyc a person login to admin panel from here:  https://django-custom-auth-model.herokuapp.com/admin/ and  modify it

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

## Demo

Available at: https://django-project-api-crud-graphq.herokuapp.com/

admin login details:--
username: admin@arpansahu.me
password: showmecode
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation

Installing Pre requisites

```bash
  pip install -r requirements.txt

```

Making Migrations and Migrating them.

```bash
  python manage.py makemigrations
  python manage.py migrate

```

Creating Super User

```bash
  python manage.py createsuperuser

```

Run Server
```bash
  python manage.py runserver

```

## Tech Stack

**Client:** HTML, Jinja, CSS, BootStrap

**Server:** Django, Gunicorn, Heroku


## Deployment on Heroku

Installing Heroku Cli from : https://devcenter.heroku.com/articles/heroku-cli
Create your account in Heroku.

Inside your project directory

Login Heroku CLI
```bash
  heroku login

```

Create Heroku App

```bash
  heroku create [app_name]

```

Push Heroku App
```
    git push heroku master
```

Configure Heroku App
```bash
  add all the env variables used from app setting page on heroku app dashboard.

```
Configuring Django App for Heroku
```
    install whitenoise : pip install whitenoise 
    include it in included_apps=[]
    add whitenoise middleware
    add: procfile
    add: release-task.sh for running mutilple commands in run: section of procfile, 
    make relase-task.sh executable : chmod +x release-tasks.sh 
```
## Documentation

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

SECRET_KEY=

DEBUG=

DB_HOST=

DB_NAME=

DB_USER=

DB_PASSWORD=

DB_PORT=

EMAIL_USER=

EMAIL_PASS=

ALLOWED_HOSTS=

