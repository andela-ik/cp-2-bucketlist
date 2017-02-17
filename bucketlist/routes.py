from flask_restful import Api
from bucketlist.views import Auth, BucketList, BucketListItem, Index

api = Api()

#default url
api.add_resource(Index, '/')

#route to handle user registration and login
api.add_resource(Auth, '/auth/<string:action>')

#create and list bucket lists
#get, update and delete single bucket list
api.add_resource(BucketList, '/bucketlists/<int:id>')

#create, update and delete item in bucket list
api.add_resource(BucketListItem, '/bucketlists/<int:id>/items/<int:item_id>')
