from flask import Flask, request
from flask_restful import Api
from bucketlist.models import db
from bucketlist.routes import api
from bucketlist.views import Index

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.app = app
db.init_app(app)
db.create_all()
api.init_app(app)
#postgresql://username:password@host:port/database

if __name__ == "__main__":
    app.run()
