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
        run.app.config.from_object('config.Testing')
        app = run.app.test_client()
        db.create_all()
        return app

    def create_test_user(self):
        url = "/auth/register"
        payload = {"name": name, "email": email, "password": password}
        self.app.post(url, data=payload)

    def create_test_bucket_list(self):
        url = "/bucketlists"
        payload = {"name": "test"}
        response = self.app.post(url, data=payload, headers=self.headers)
        print(response.headers)

    def login_test_user(self):
        url = "/auth/login"
        payload = {"email": email, "password": password}
        response = self.app.post(
            url, data=payload)
        response = json.loads(response.data)
        print(response)
        return response

    def setUp(self):
        self.app = self.init_test_app()
        self.create_test_user()
        self.access_token = self.login_test_user()["access_token"]
        self.headers = {"access_token": self.access_token}
        self.create_test_bucket_list()
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
