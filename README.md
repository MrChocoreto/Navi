# Navi

## About
Navi it's an API REST created in python using Django and Django Rest Framework. This project was used in an web app for UDEM (Morelia's Univerty).

## Installation 

Clone the repository

```sh
git clone https://github.com/MrChocoreto/Navi.git 
```

## Setup Project
You might have python 3.12.2 intalled in your device.

You can ensure that is installed using this comand
```sh
python --version
```
If you dont have install this version go to the official page to download.

[python.org/downloads](https://www.python.org/downloads/)

### Dependencies
>[!NOTE]
>To create the environment the command works same for Linux and Windows. 

>[!NOTE]
>I recommend create the environment if you're only work in local 



First you have to create your environment to have more control in the project
```sh
python -m venv env
```
Now you have execute the environment before to install the dependencies. To execute this commands you need be in the project path. 

#### Windows

```sh
./env/Scripts/activate
```

#### Linux
```sh
source ./env/bin/activate
```

After that you need install the next dependencies:
- setuptools

```sh
pip install setuptools
```
- django

```sh
pip install django 
```
- django rest framework

```sh
pip install djangorestframework
```
- coreapi

```sh
pip install coreapi
```

- mysql

```sh
pip install mysqlclient
```

### DataBase Setup

To use the database you need create the next configuration in MariaDB

- user: ```navi```
- password: ```1>fCT)},dfVZ6Rbv9q*.```
- port: ```3306```
- host: ```localhost```

To create the user in database if is not created:
```sql
CREATE USER 'navi'@localhost IDENTIFIED BY '1>fCT)},dfVZ6Rbv9q*';
```
Then, give it the correct access to the database
```sql
GRANT USAGE ON *.* TO 'navi'@localhost IDENTIFIED BY '1>fCT)},dfVZ6Rbv9q*'
```

### Initialize API

After to run the API you might do the next commands.
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```


For the test in local you have to write this command.
```sh
python manage.py runserver
```

### Exit Environment

If you want to exit of your environment you need put the next command:

```sh
deactivate
```

