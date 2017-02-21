import bcrypt
from sqlalchemy import Column, Integer, String, Boolean,  ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class DateMixin(object):
    date_created = Column(DateTime, default=func.now())
    date_modified = Column(DateTime, onupdate=func.now())


class Base(object):
    id = Column(Integer, primary_key=True)
    name = Column(String(120))


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(cls=Base)


class User(db.Model, DateMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    name = Column(String(120), unique=False)
    password = Column(String(120))
    bucketlists = relationship("BucketList", back_populates="user")

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.password = hash
        db.session.add(self)
        db.session.commit()

    def verify_password(self, password):
        password = password.encode('utf-8')
        if bcrypt.hashpw(password, self.password) == self.password:
            return True

    def __repr__(self):
        return '<User %r>' % (self.name)


class BucketList(db.Model, Base, DateMixin):
    __tablename__ = 'bucketlist'
    created_by = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="bucketlists")
    items = relationship("Item", back_populates="bucketlist")

    def __init__(self, name, user_id):
        self.name = name.title()
        self.created_by = user_id
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        bucketlist = {}
        bucketlist['id'] = self.id
        bucketlist['name'] = self.name
        bucketlist['items'] = []
        if self.items:
            for item in self.items:
                bucketlist['items'].append(item.__repr__())
        bucketlist['date_created'] = "{}".format(self.date_created)
        bucketlist['date_modified'] = "{}".format(self.date_modified)
        bucketlist['created_by'] = self.user.name
        return bucketlist


class Item(db.Model, Base, DateMixin):
    __tablename__ = 'item'
    status = Column(Boolean, default=False)
    bucketlist_id = Column(Integer, ForeignKey('bucketlist.id'))
    bucketlist = relationship("BucketList", back_populates="items")

    def __init__(self, name, bucketlist):
        self.name = name
        self.bucketlist_id = bucketlist
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        item = {}
        item['id'] = self.id
        item['name'] = self.name
        item['date_created'] = "{}".format(self.date_created)
        item['date_modified'] = "{}".format(self.date_modified)
        item['done'] = self.status
        return item
