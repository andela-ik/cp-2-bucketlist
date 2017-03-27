from test.base_test import BaseTest
from bucketlist.models import BucketList

test = BucketList.query.first()
id = test.id
url = "bucketlists/{}/items".format(id)


class BucketListTestItem(BaseTest):

    def test_create_bucketlist_item(self):
        payload = {"name": "Item 1"}
        response = self.app.post(url, data=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn("location", response.headers)

    def test_update_bucketlist_item(self):
        payload = {"name": "Item Updated"}
        response = self.app.put(
            url + "/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("deleted", response.data.decode())

    def test_delete_bucketlist_item(self):
        response = self.app.delete(
            url + "/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("deleted", response.data.decode())
