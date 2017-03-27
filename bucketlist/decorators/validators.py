from functools import wraps
from bucketlist.models import db, User, BucketList
from validate_email import validate_email
from flask import request
import re
from bucketlist.templates.errors import *

MIN_PASSWORD_LENGTH = 8
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}'


def validate_register_data(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "name" not in request.form:
            return {"error": "Enter Your Name"}, 422
        if len(request.form['name']) == 0:
            return {"error": "Enter Your Name"}, 422

        if "email" not in request.form:
            return make_404_error("Enter Email Address")
        if "password" not in request.form:
            return make_404_error("Enter Password")

        email = request.form["email"]

        if validate_email(email):
            if len(User.query.filter_by(email=email).all()) > 0:
                return {"error": "This email address has already been registered"}, 409
        else:
            return {"message": "invalid email address"}, 422

        if validate_password(request.form["password"]):
            password = request.form["password"]
        else:
            return {"message": "password must be alphanumeric and 8 characters long "}, 422

        return func(*args, **kwargs)
    return decorated_function


def validate_login_data(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "email" not in request.form:
            return make_404_error("Enter Email Address")
        if "password" not in request.form:
            return make_404_error("Enter Password")
        return func(*args, **kwargs)
    return decorated_function


def validate_password(password):
    if re.search(PASSWORD_REGEX, password):
        return True


def validate_bucket_list_data(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "name" in request.form:
            bucketlist_name = request.form["name"]
        else:
            return {"error": "Enter bucketlist name"}, 400
        user_id = kwargs['user']
        user_bucket_lists = BucketList.query.filter_by(
            name=bucketlist_name.title(), created_by=user_id).all()
        if len(user_bucket_lists) > 0:
            return {"error": "Bucket List Exists"}, 409

        return func(*args, **kwargs)
    return decorated_function


def validate_bucket_list_item_data(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):

        if "id" in kwargs:
            bucket_id = kwargs["id"]

        user_id = kwargs['user']
        user_bucket_list = BucketList.query.filter_by(
            bucket_id=bucket_id, created_by=user_id).first()
        if user_bucket_list:
            if request.method == 'POST':
                if "name" in request.form:
                    item_name = request.form["name"]
                    if item_name in [item.name for item in user_bucket_list.items]:
                        return make_404_error("Item Exists in this bucketlist")
                else:
                    return make_404_error("Invalid Request")
            print(kwargs)
            return func(*args, **kwargs, bucketlist=user_bucket_list)
        else:
            return make_404_error("Not Found")

    return decorated_function
