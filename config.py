import tempfile


class Default(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Change This
    SECRET_KEY = "\xffI\x9b\xb4\x147\n\x88y+2\xeef\xd1\x1d\xae\xa8\xfa\xdf\xb7"
    JSON_SORT_KEYS = False


class Production(Default):
    DATABASE_USER = "postgres"
    DATABASE_PASSWORD = ""
    DATABASE_HOST = "localhost"
    DATABASE_NAME = "buckets"
    DATABASE_PORT = "5432"
    SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@{}:{}/{}'.format(
        DATABASE_USER,
        DATABASE_PASSWORD,
        DATABASE_HOST,
        DATABASE_PORT,
        DATABASE_NAME
    )
    DEBUG = True


class Development(Default):
    DEBUG = True


class Testing(Default):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        tempfile.mkstemp()[1]
