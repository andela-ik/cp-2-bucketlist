from test.base_test import BaseTest
import json

url = "/bucketlists"


class BucketListTest(BaseTest):

    def test_create_bucketlist(self):
        payload = {"name": "bucketlist 1"}
        response = self.app.post(url, data=payload, headers=self.headers)
        assert response.status, 201
        assert "location" in response.headers
        response = json.loads(response.data)
        print(response)
