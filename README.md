# Stackoverflow Shipmnts

**A [Django](https://www.djangoproject.com/) Application**

## Prerequistics

* Python3
* Mysql
* Virtualenv

## Installation and Setup

* Setup a virtualenv
    ```bash
        virtualenv -p python3 <foldername>
    ```
* Clone the **Git** repository.
* Create a database
* Navigate to the project root folder and install all the dependecies
    ```bash
        pip install -r requirements.txt
    ```
* Setup the database configurations in project root **settings.py**
    ```bash
        DATABASES = {

        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'name of database',
            'USER':'username',
            'PASSWORD':'password',
            'HOST':'localhost',
            'PORT':'3306',
            }
        }
    ```

* Migrate all the models to the database
    ```python
         python manage.py makemigrations
         python manage.py migrate
    ```
* Create a super user to access django admin panel.Admin panel can be accessed at http://localhost:8000/admin
    ```python
        python manage.py createsuperuser
    ```
* Start the server in terminal.Home page can be accessed at http://localhost:8000/enterprise/home
    ```python
        python manage.py runserver
    ```
