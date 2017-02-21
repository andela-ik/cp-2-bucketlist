from functools import wraps
import jwt
from jwt import InvalidTokenError
from bucketlist.models import User
from flask import request

secret = "\xffI\x9b\xb4\x147\n\x88y+2\xeef\xd1\x1d\xae\xa8\xfa\xdf\xb7"


def check_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not "Api-Key" in request.headers:
            return{"error": "Unauthorized"}, 401
        try:
            user_id = jwt.decode(request.headers['Api-Key'], secret)
            user = User.query.filter_by(id=user_id['id']).first()
            if not user:
                return{"error": "Invalid Credentials"}, 401
            return func(*args, user=user_id['id'])
        except InvalidTokenError:
            return{"error": "Invalid Credentials"}, 401
    return wrapper
