from flask import Flask, request
from flask_restful import Resource
import jwt
from bucketlist.models import db, User, BucketList
from bucketlist.decorators.validators import validate_user_input
from bucketlist.decorators.auth import check_api_key

secret = "\xffI\x9b\xb4\x147\n\x88y+2\xeef\xd1\x1d\xae\xa8\xfa\xdf\xb7"


class Auth(Resource):

    def post(self, action):
        if action.lower() == "login":
            return self.login(request)

        elif action.lower() == "register":
            return self.register(request)
        else:
            return {"error": "bad route"}, 404

    def login(self, request):
        user = User.query.filter_by(email=request.form["email"]).first()
        if not user or not user.verify_password(request.form["password"]):
            return {"error": "wrong username/password"}

        token = jwt.encode({'id': user.id}, secret, algorithm='HS256')
        return {
            "message": "login successful",
            "access_token": token.decode('utf-8')
        }

    @validate_user_input
    def register(self, request):
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
        return {"message": "Signup Successful"}, 201


class BucketLists(Resource):

    def get(self, id=None):
        if id:
            # Get single bucket list
            pass
        else:
            # List all the created bucket lists
            pass

    @check_api_key
    def post(self, id=None):
        if id:
            # Throw error
            pass
        else:
            # Create a new bucket list
            pass

    def put(self, id=None):
        # Update this bucket list
        if id:
            # Update this bucket list
            pass
        else:
            # Throw error
            pass

    def delete(self, id=None):
        if id:
            # Delete this single bucket list
            pass
        else:
            # Throw error
            pass


class BucketListItem(Resource):

    def post(self, id=None, item_id=None):
        # Create a new item in bucket list
        pass

    def put(self, id=None, item_id=None):
        # Update a bucket list item
        pass

    def delete(self, id=None, item_id=None):
        # Delete an item in a bucket list
        pass
