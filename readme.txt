# REST API Project

## Description
This RESP API has endpoints to Get, Post, Put and Delete Items and stores. When retrieving a store the list of items associated to that store is also retrieved.

There are also end points to register users and for users to authenticate themselves.

Only successfully authenticated users are able to hit the Item and Store endpoints successfully. Authorisation is done using JWT_Token.

## SETUP
clone 'code' repository
create venv in sibling directory
install the libraries below (using 'pip install' or pycharm installer etc)
Flask
Flask-JWT
Flask-RESTful
Flask-SQLAlchemy

mark /code directory as sources root

##RUN
remove data.db (if exists)

enter venv
navigate to /code
run create_table.py
# this creates the necessary tables and creates data.db
run app.py
# runs the app on port 5000
hit the end points
