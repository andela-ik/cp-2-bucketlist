def make_400_error(message):
    """ Invlaid request errors"""
    return {"error": "{}".format(message)}, 400


def make_401_error(message):
    """ Unauthorized Request"""
    headers = {"WWW-Authenticate": "access_token=token"}
    return {"error": "{}".format(message)}, 401, headers


def make_404_error(message):
    """ Invlaid request errors"""
    return {"error": "{}".format(message)}, 404


def make_409_error(message):
    """ Resource Conflict Errors"""
    return {"error": "{}".format(message)}, 409


def make_422_error(message):
    """" Input validation errors"""
    return {"error": "{}".format(message)}, 422
