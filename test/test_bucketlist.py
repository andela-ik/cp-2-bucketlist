from test.base_test import BaseTest
from bucketlist.models import BucketList
import json

url = "/bucketlists"


class BucketListTest(BaseTest):

    def test_create_bucketlist(self):
        payload = {"name": "bucketlist 1"}
        response = self.app.post(url, data=payload, headers=self.headers)
        print(response)
        self.assertEqual(response.status_code, 201)
        self.assertIn("location", response.headers)
        response = json.loads(response.data)

    def test_create_bucket_list_name_validation(self):
        payload = {"name": "test"}
        response = self.app.post(url, data=payload, headers=self.headers)
        self.assertEqual(response.status_code, 409)
        self.assertNotIn("location", response.headers)

    def test_update_bucketlist(self):
        payload = {"name": "test2"}
        self.create_test_bucket_list()
        test = BucketList.query.first()
        print(test.id)
        response = self.app.put(
            url + "/" + str(test.id), data=payload, headers=self.headers)
        print(response.data.decode())
        self.assertIn("Updated", response.data.decode())

    def test_delete_bucketlist(self):
        initial_count = len(BucketList.query.all())
        response = self.app.delete(url + "/1", headers=self.headers)
        count_after = len(BucketList.query.all())
        self.assertEqual(count_after, initial_count - 1)
