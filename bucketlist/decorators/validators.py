from functools import wraps
from bucketlist.models import db, User, BucketList
from validate_email import validate_email
from flask import request
import re

MIN_PASSWORD_LENGTH = 8
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}'


def validate_user_input(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        request = args[1]
        name = request.form["name"]
        email = request.form["email"]
        if validate_password(request.form["password"]):
            password = request.form["password"]
        else:
            return {"error": "password must be alphanumeric and 8 characters long "}

        if validate_email(email):
            if len(User.query.filter_by(email=email).all()) > 0:
                return {"error": "This email address has already been registered"}, 409
        else:
            return {"error": "invalid email address"}
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
        print(kwargs)
        user_id = kwargs['user']
        user_bucket_lists = BucketList.query.filter_by(
            name=bucketlist_name.title(), created_by=user_id).all()
        if len(user_bucket_lists) > 0:
            return {"error": "error message"}, 409

        return func(*args, **kwargs)
    return decorated_function


def validate_bucket_list_item_data(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "name" in request.form:
            item_name = request.form["name"]

        if "id" in kwargs:
            bucket_id = kwargs["id"]

        print(kwargs)
        user_id = kwargs['user']
        user_bucket_lists = BucketList.query.filter_by(
            name=bucketlist_name.title(), created_by=user_id).all()
        if len(user_bucket_lists) > 0:
            return {"error": "error message"}, 409

        return func(*args, **kwargs)
    return decorated_function
