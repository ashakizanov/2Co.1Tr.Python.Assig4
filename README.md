# 2Co.1Tr.Python.Assig4

## TITLE

Assignment 4

## Installation
PyPl
``` bash 
pip install flask
pip install flask-sqlalchemy
pip install bs4
pip install requests
```

## Usage
```bash
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup
from sqlalchemy import desc
```

## connect to DataBase
```bash
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PASSWORD@localhost/CoinMarket'
db = SQLAlchemy(app)


postgresql://user:passwoed@localhost/mydatabase
mysql://user:passwoed@localhost/mydatabase
oracle://user:passwoed@127.0.0.1:1521/mydatabase
```


#Examples
```bash
https://github.com/selfedu-rus/flsite_sqlalchemy-23
https://www.section.io/engineering-education/flask-database-integration-with-sqlalchemy/
```

##Sources
```bash
pyjwt (https://pyjwt.readthedocs.io/en/stable/)
flask (https://flask.palletsprojects.com/en/2.0.x/)
flask_sqlalchemy (https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
requests  (https://pypi.org/project/requests/)
beautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
```
# Done by
Amirkhan Shakizan
Altair Tussupov
