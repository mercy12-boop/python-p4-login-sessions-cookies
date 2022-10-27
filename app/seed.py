from app import app
from models import db, GroceryItem, User

db.init_app(app)

with app.app_context():

    print("Deleting users...")
    User.query.delete()

    print("Deleting groceries...")
    GroceryItem.query.delete()

    print("Creating User object...")
    user = User(username="myuser", password="password")
    
    print("Creating User record...")
    db.session.add(user)

    print("Creating GroceryItem objects...")
    steak = GroceryItem(name="Ribeye Steak", price=11, user=user)
    apple = GroceryItem(name="Apple", price=1, user=user)
    waterloo_twelve_pack = GroceryItem(name="Waterloo 12 Pack", price=6, user=user)

    print("Creating GroceryItem records...")
    db.session.add_all([steak, apple, waterloo_twelve_pack])
    db.session.commit()

    print("Complete.")
