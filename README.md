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

# Unit Test
```sh
$ python test/article_test.py
```

# Demo:
1. Go to localhost:8080
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot1.png)

2. For the first time, create article. All data must be filled.
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot2.png)

3. Click the 'Create' button, if success, flash message 'Article created successfully' will appear. Click return to articles to going back to home
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot3.png)

4. New data appear!
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot4.png)

5. Lets create one more. And now let we click edit on first data
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot5.png)

6. Edit title, and update it
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot6.png)

7. On the first article, title changed.
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot7.png)

8. Lets delete second article, click delete. You will see new page, click 'Delete Article' for confirmation. 
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot8.png)

9. Second data has been deleted. Lets do one more with the only one data 
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot9.png)

10. Click 'Delete Article'
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot10.png)

11. Puff! All data gone!
![Empty data](https://raw.githubusercontent.com/ardinusawan/Flask-VueJS-CRUD-Sample/master/screenshot/screenshot11.png)

License
----

MIT

**Free Software, Hell Yeah!**

