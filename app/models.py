from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class GroceryItem(db.Model, SerializerMixin):
    __tablename__ = 'grocery_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<GroceryItem {self.name} | Price: ${self.price}>'
