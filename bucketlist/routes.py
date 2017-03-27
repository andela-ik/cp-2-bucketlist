from flask_restful import Api
from bucketlist.views import Auth, BucketLists, BucketListItem, Index

api = Api()

version = "/api/v1"
# route to github repository
api.add_resource(Index, '{}/'.format(version))

# route to handle user registration and login
api.add_resource(Auth, '{}/auth/<string:action>'.format(version))

# create and list bucket lists
# get, update and delete single bucket list
api.add_resource(BucketLists, '{}/bucketlists'.format(version),
                 '{}/bucketlists/<int:id>'.format(version))

# create, update and delete item in bucket list
api.add_resource(BucketListItem, '{}/bucketlists/<int:id>/items'.format(version),
                 '{}/bucketlists/<int:id>/items/<int:item_id>'.format(version))
