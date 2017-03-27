# Buckets
>A Bucket List is a list of things that one wants to do before they die.

This is an API that can be used to create and monitor bucket lists.

## Installation

### Dependencies
* Python 3.6
* Flask
* Flask-RESTful

```

git clone https://github.com/andela-ik/cp-2-bucketlist.git
cd cp-2-bucketlist
pip install -r requirements.txt

```

## Running

There are 3 different configurations available:

* Development
* Testing
* Production


#### Development
open `manage.py` and set: `app.config.from_object('config.Development')`

#### Testing
open `manage.py` and set: `app.config.from_object('config.Testing')`

#### Production
This is specifically set to use postgres

Reuires: `psycopg2==2.7.1`

open `manage.py` and set: `app.config.from_object('config.Production')`

Execute: `python manage.py runserver`
