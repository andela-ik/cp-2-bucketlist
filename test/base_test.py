import os
import run
import unittest
import tempfile
from bucketlist.models import db, User
import json

name = "ian"
email = "an@asas.co"
password = "password123A"


class BaseTest(unittest.TestCase):

    def init_test_app(self):
        run.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
            tempfile.mkstemp()[1]
        run.app.config['TESTING'] = True
        app = run.app.test_client()
        db.create_all()
        return app

    def create_test_user(self):
        url = "/auth/register"
        payload = {"name": name, "email": email, "password": password}
        self.app.post(url, data=payload)

    def login_test_user(self):
        url = "/auth/login"
        payload = {"email": email, "password": password}
        response = self.app.post(
            url, data=payload)
        response = json.loads(response.data)
        return response

    def setUp(self):
        self.app = self.init_test_app()
        self.create_test_user()
        self.access_token = self.login_test_user()["access_token"]
        self.headers = {"access_token": self.access_token}
        # TODO: create test bucket list and item

    #
    # def test_listall_bucketlist(self):
    #     url = "/bucketlists"
    #     payload = {}
    #     response = self.app.get(url)
    #
    # def test_get_one_bucketlist(self):
    #     url = "/bucketlists/1"
    #     payload = {}
    #     response = self.app.get(url)
    #
    # def test_update_bucketlist(self):
    #     url = "/bucketlists/1"
    #     payload = {}
    #     response = self.app.put(url, data=payload)
    #
    # def test_delete_bucketlist(self):
    #     url = "/bucketlists/1"
    #     payload = {}
    #     response = self.app.delete(url, data=payload)
    #
    # def test_create_bucketlist_item(self):
    #     url = "/bucketlists/1/items"
    #     payload = {}
    #     response = self.app.post(url, data=payload)
    #
    # def test_update_bucketlist_item(self):
    #     url = "/bucketlists/1/items/1"
    #     payload = {}
    #     response = self.app.put(url, data=payload)
    #
    # def test_delete_bucketlist_item(self):
    #     url = "/bucketlists/1/items/1"
    #     payload = {}
    #     response = self.app.put(url, data=payload)

    def tearDown(self):
        # os.close(self.db_fd)
        # os.unlink(run.app.config['SQLALCHEMY_DATABASE_URI'])
        pass

if __name__ == '__main__':
    unittest.main()
