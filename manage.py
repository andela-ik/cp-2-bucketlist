from flask import Flask, request
from flask_restful import Api
from bucketlist.models import db
from bucketlist.routes import api
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config[
    'SECRET_KEY'] = "\xffI\x9b\xb4\x147\n\x88y+2\xeef\xd1\x1d\xae\xa8\xfa\xdf\xb7"
app.config["JSON_SORT_KEYS"] = False
app.config["DEBUG"] = True

db.app = app
db.init_app(app)
db.create_all()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
api.init_app(app)
# postgresql://username:password@host:port/database

if __name__ == "__main__":
    manager.run()
