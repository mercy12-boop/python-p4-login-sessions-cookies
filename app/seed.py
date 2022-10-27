from app import app
from models import db, GroceryItem

db.init_app(app)

with app.app_context():

    print("Deleting groceries...")
    GroceryItem.query.delete()

    print("Creating GroceryItem objects...")
    steak = GroceryItem(name="Ribeye Steak", price=11)
    apple = GroceryItem(name="Apple", price=1)
    waterloo_twelve_pack = GroceryItem(name="Waterloo 12 Pack", price=6)

    print("Creating GroceryItem records...")
    db.session.add_all([steak, apple, waterloo_twelve_pack])
    db.session.commit()

    print("Complete.")
