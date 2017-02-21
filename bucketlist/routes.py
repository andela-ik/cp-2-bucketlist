from flask_restful import Api
from bucketlist.views import Auth, BucketLists, BucketListItem

api = Api()

# route to handle user registration and login
api.add_resource(Auth, '/auth/<string:action>')

# create and list bucket lists
# get, update and delete single bucket list
api.add_resource(BucketLists, '/bucketlists', '/bucketlists/<int:id>')

# create, update and delete item in bucket list
api.add_resource(BucketListItem, '/bucketlists/<int:id>/items',
                 '/bucketlists/<int:id>/items/<int:item_id>')
