from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cover_photo = db.Column(db.String(120), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
