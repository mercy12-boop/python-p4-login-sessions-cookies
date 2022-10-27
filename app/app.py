#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, GroceryItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Groceries(Resource):

    def get(self):
        groceries = [grocery_item.to_dict() for grocery_item in GroceryItem.query.all()]
        return make_response(jsonify(groceries), 200)

    def post(self):

        data = request.get_json()

        grocery_item = GroceryItem(
            name=data['name'],
            price=data['price'],
        )

        db.session.add(grocery_item)
        db.session.commit()

        return make_response(jsonify(grocery_item.to_dict()), 201)

api.add_resource(Groceries, '/groceries')

class GroceryItemByID(Resource):

    def get(self, id):
        grocery_item = GroceryItem.query.filter_by(id=id).first().to_dict()
        return make_response(jsonify(grocery_item), 200)

    def patch(self, id):

        data = request.get_json()

        grocery_item = GroceryItem.query.filter_by(id=id).first()

        for attr in data:
            setattr(grocery_item, attr, data[attr])

        db.session.add(grocery_item)
        db.session.commit()

        return make_response(jsonify(grocery_item.to_dict()), 200)

    def delete(self, id):

        grocery_item = GroceryItem.query.filter_by(id=id).first()
        db.session.delete(grocery_item)
        db.session.commit()

        return make_response(jsonify({'message': "item deleted"}), 204)

api.add_resource(GroceryItemByID, '/groceries/<int:id>')
        

if __name__ == '__main__':
    app.run(port=5555)
