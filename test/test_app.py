import os
import run
import unittest
import tempfile
from bucketlist.models import db, User

class FlaskrTestCase(unittest.TestCase):
    def init_test_app(self):
        run.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + tempfile.mkstemp()[1]
        run.app.config['TESTING'] = True
        app = run.app.test_client()
        db.create_all()
        return app

    def setUp(self):
        self.app = self.init_test_app()
        #TODO: create test bucket list and item
        url = "/auth/register"
        name = "ian"
        email = "an@asas.co"
        payload = {"name": name, "email":email, "password":"password123A"}
        response = self.app.post(url, data = payload)


    def test_login(self):
        url = "/auth/login"
        payload= {"username": "ian", "password": "demo1234"}
        response = self.app.post(url, data = payload)


    def test_register(self):
        url = "/auth/register"
        name = "ian"
        email = "an@asas.co"
        payload = {"name": name, "email":email, "password":"password"}
        response = self.app.post(url, data = payload)
        new_user = User.query.filter_by(name = name).one()
        self.assertEqual(new_user.name, name)

    def test_create_bucketlist(self):
        url = "/bucketlists"
        payload = { }
        response = self.app.post(url)

    def test_listall_bucketlist(self):
        url = "/bucketlists"
        payload = { }
        response = self.app.get(url)

    def test_get_one_bucketlist(self):
        url = "/bucketlists/1"
        payload = { }
        response = self.app.get(url)

    def test_update_bucketlist(self):
        url = "/bucketlists/1"
        payload = { }
        response = self.app.put(url, data = payload)

    def test_delete_bucketlist(self):
        url = "/bucketlists/1"
        payload = { }
        response = self.app.delete(url, data = payload)

    def test_create_bucketlist_item(self):
        url = "/bucketlists/1/items"
        payload = { }
        response = self.app.post(url, data = payload)

    def test_update_bucketlist_item(self):
        url = "/bucketlists/1/items/1"
        payload = { }
        response = self.app.put(url, data = payload)

    def test_delete_bucketlist_item(self):
        url = "/bucketlists/1/items/1"
        payload = { }
        response = self.app.put(url, data = payload)



    def tearDown(self):
        #os.close(self.db_fd)
        #os.unlink(run.app.config['SQLALCHEMY_DATABASE_URI'])
        pass

if __name__ == '__main__':
    unittest.main()
