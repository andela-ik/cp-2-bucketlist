from flask import Flask, request
from flask_restful import Resource
from bucketlist.models import db, User
from bucketlist.utils.validators import validate_user_input

class Index(Resource):
    def get(self):
        return {"App Test":"I Work"}

    def post(self):
        print(dict(request.form))
        return {"App Test":"I Still Work"}

class Auth(Resource):

    def post(self, action):
        if action.lower() == "login":
            return self.login(request)

        elif action.lower() == "register":
            return self.register(request)
        else:
            return {"error": "bad route"}, 404

    def login(self, request):
        return {"message":"login successful"}

    @validate_user_input
    def register(self, request):
        print("here")
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
        return {"message":"Signup Successful"}, 201

class BucketList(Resource):
    def get(self, id = None):
        if id:
            #Get single bucket list
            pass
        else:
            #List all the created bucket lists
            pass

    def post(self, id = None):
        if id:
            #Throw error
            pass
        else:
            #Create a new bucket list
            pass

    def put(self, id = None):
        #Update this bucket list
        if id:
            #Update this bucket list
            pass
        else:
            #Throw error
            pass

    def delete(self, id = None):
        if id:
            #Delete this single bucket list
            pass
        else:
            #Throw error
            pass

class BucketListItem(Resource):

    def post(self, id = None, item_id = None):
        #Create a new item in bucket list
        pass
    def put(self, id = None, item_id = None):
        #Update a bucket list item
        pass

    def delete(self, id = None, item_id = None):
        #Delete an item in a bucket list
        pass
