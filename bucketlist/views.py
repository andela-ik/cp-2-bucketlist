import jwt
from bucketlist.decorators.auth import check_access_token
from bucketlist.decorators.validators import *
from bucketlist.models import BucketList, Item, User, db
from bucketlist.templates.errors import *
from bucketlist.templates.messages import *
from bucketlist.utils.utils import paginate_data
from flask import Flask, request, redirect, url_for
from flask_restful import Resource

secret = "\xffI\x9b\xb4\x147\n\x88y+2\xeef\xd1\x1d\xae\xa8\xfa\xdf\xb7"


class Index(Resource):

    def get(self):
        return redirect("https://github.com/andela-ik/cp-2-bucketlist", 301)


class Auth(Resource):

    def post(self, action):
        print(request.data)
        if action.lower() == "login":
            return self.login(request)

        elif action.lower() == "register":
            return self.register(request)
        else:
            return {"error": "bad route"}, 404

    @validate_login_data
    def login(self, request):
        user = User.query.filter_by(email=request.form["email"]).first()
        if not user or not user.verify_password(request.form["password"]):
            return {"message": "wrong username/password"}

        token = jwt.encode({'id': user.id}, secret, algorithm='HS256')
        response = {
            "message": "login successful",
            "access_token": token.decode('utf-8')

        }
        return response

    @validate_register_data
    def register(self, request):
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(name, email, password)
        return make_message("Signup Successful", 201, None)


class BucketLists(Resource):

    @check_access_token
    def get(self, id=None, user=None):
        url = ("{}{}").format(request.host, request.path)
        # Fetch One
        if id:
            bucketlist = BucketList.query.filter_by(
                bucket_id=id, created_by=user).first()
            if bucketlist:
                return bucketlist.__repr__()
            else:
                return make_404_error("bucketlist doesn't exist")

        else:
            # Search Function
            parameter = request.args['q'] if 'q' in request.args else ''
            return self.search(user, url, parameter)

    def search(self, user, url, parameter):
        offset = request.args['offset'] if 'offset' in request.args else 1
        limit = request.args['limit'] if 'limit' in request.args else 20

        bucketlists_query = BucketList.query.filter(
            BucketList.name.contains(parameter)).filter_by(created_by=user)

        bucketlists, info, headers = paginate_data(
            bucketlists_query, int(limit), int(offset), url)

        data = {}
        data.update(info)
        data["bucketlists"] = []
        for bucketlist in bucketlists:
            data["bucketlists"].append(bucketlist.__repr__())

        return(data, 200, headers)

    @check_access_token
    @validate_bucket_list_data
    def post(self, id=None, user=None):
        url = request.path + "/{}"
        if user:
            name = request.form["name"]
            user_id = user
            bucketlist = BucketList(name, user_id)
            response = {"message": "Bucket List created successfuly"}
            header = {"location": url.format(str(bucketlist.bucket_id))}
            return response, 201, header

    @check_access_token
    @validate_bucket_list_data
    def put(self, id=None, user=None):
        # Update this bucket list
        if id:
            # Update this bucket list
            bucketlist = BucketList.query.filter_by(
                bucket_id=id, created_by=user).first()
            if bucketlist:
                bucketlist.name = request.form['name']
                bucketlist.save()
                return {"message": "Bucketlist Updated Successfully"}, 200
            else:
                return make_404_error("Bucket List Doesn't exist")
        else:
            return make_404_error("No bucketlist specified for the requested operation")

    @check_access_token
    def delete(self, id=None, user=None):
        if id:
            # Delete this single bucket list
            bucketlist = BucketList.query.filter_by(
                bucket_id=id, created_by=user).first()
            if bucketlist:
                bucketlist.delete()
                return {"message": "Bucketlist Deleted Successfully"}, 200
            else:
                return make_404_error("Bucket List Doesn't exist")


class BucketListItem(Resource):

    @check_access_token
    @validate_bucket_list_item_data
    def post(self, id, user=None, bucketlist=None):
        url = request.path + "/{}"
        # Create a new item in bucket list
        if id:
            name = request.form['name']
            bucketlist_item = Item(name, bucketlist.id)
            response = {"message": "Item Added Successfuly"}
            header = {"location": url.format(str(bucketlist_item.item_id))}
            return make_message(response, 201, header)

    @check_access_token
    @validate_bucket_list_item_data
    def put(self, id=None, item_id=None, user=None, bucketlist=None):
        # Update a bucket list item
        status = request.form['status']
        item = Item.query.filter_by(
            bucketlist_id=bucketlist.id, item_id=item_id).first()
        if item:
            item.status = status
            item.save()
            return make_message("Item Updated Successfully", 200)
        else:
            return make_404_error("Item does not exist")

    @check_access_token
    @validate_bucket_list_item_data
    def delete(self, id=None, item_id=None, user=None, bucketlist=None):
        # Delete an item in a bucket list
        item = Item.query.filter_by(
            bucketlist_id=bucketlist.id, item_id=item_id).first()
        if item:
            item.delete()
            return make_message("Item deleted successfully", 200)
        else:
            return make_404_error("Item does not exist")
