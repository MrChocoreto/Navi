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
>This works for Linux and Windows. 


First you have to create your environment to have more control in the project
```sh
python -m venv 'environment-name'
```
After you need install need install the next dependencies:
- setuptools
- django
- djangorestframework
- coreapi

To install them use this comand changing *"package"* by the name of the dependencie
```sh
pip install 'package'
```

### Test API

For the test in local you have to write this command.
```sh
python manage.py runserver
```

