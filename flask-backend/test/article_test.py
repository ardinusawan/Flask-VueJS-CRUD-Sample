# project/test_basic.py
 
 
import os
import unittest
import sys 
# from project import app, db, mail
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from PIL import Image
# import requests
# from io import BytesIO
from article import *
# export FLASK_APP=article.py

TEST_DB = 'test.db'
# BASEDIR = '.'
# response = requests.get('https://www.google.org/assets/static/images/logo_googledotorg-171e7482e5523603fc0eed236dd772d8.svg')
# thumnbail = Image.open(BytesIO(response.content))
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            # os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        # Disable sending emails during unit testing
        # mail.init_app(app)
        # self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/article', follow_redirects=True)
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_delete_page(self, id="1"):
        response = self.app.get('/article/'+id, follow_redirects=True)
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()