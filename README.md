# Frontend
How to run:

Install dependency
```sh
$ npm install
```
Run app
```sh
$ npm run dev
```
Server run in http://localhost:8080

# Backend
How to run:

Installing virtual environment
```sh
$ virtualenv -p python3 venv
```
Load environment
```sh
$ source venv/bin/activate
```
Installing dependency
```sh
$ pip install -r requirements.txt
```
For first time instalation, create database if not exist
```sh
$ python
>>> from article import db
>>> db.create_all()
>>> exit()
```

Run app
```sh
$ python article.py
```
Server run in http://localhost:5000

License
----

MIT


**Free Software, Hell Yeah!**
