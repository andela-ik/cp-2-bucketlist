from bucketlist.models import db
from bucketlist.routes import api
from flask import Flask, request
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_script import Manager

app = Flask(__name__)

app.config.from_object('config.Development')

db.app = app
db.init_app(app)
db.create_all()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
api.init_app(app)

if __name__ == "__main__":
    manager.run()
