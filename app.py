# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Set up your database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mich:789456@localhost/mydatabase'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define your models here (example)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)
