# ----------------------------------------------------------------------
# Name:        restaurants
# Purpose:     Demonstrate web development with Flask and Alchemy
#
# Author:      Phong Trinh & Kunda Wu
# ----------------------------------------------------------------------
"""
A web application with database access to restaurants.

Point your browser to http://localhost:5000/
"""

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
db = SQLAlchemy(app)

class Restaurant(db.Model):
    """
    Class to represent and access the review table.
    Attributes:
    id (integer) : the insertion number
    name (string)   : the name of the restaurant
    location (string)   : the location of the restaurant
    category (string)   : the category of the restaurant
    price (int) :   the price of the restaurant (1 is cheap and 4 is expensive)
    """

    __tablename__ = "restaurant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)

@app.route('/')
@app.route('/home')
def welcome():
    results = Restaurant.query.all()
    if len(results) > 5:
        results = [element for element in results[-5::]]
    results.reverse()
    return render_template('home.html', results=results)

@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        name_input = request.form.get('name')
        category_input = request.form.get('category')
        location_input = request.form.get('location')
        price_input = request.form.get('price')
        new_restaurant = Restaurant(name=name_input, location=location_input,
                                    category=category_input, price=price_input)
        db.session.add(new_restaurant)
        db.session.commit()
    return render_template('add.html')

@app.route('/view', methods=["POST", "GET"])
def find():
    results = []
    location = ""
    category = ""
    price = ""
    if request.method == 'POST':
        category = request.form.get('category')
        location = request.form.get('location')
        price = request.form.get('price')
        query = Restaurant.query
        if category:
            query = query.filter(Restaurant.category == category)
        if location:
            query = query.filter(Restaurant.location == location)
        if  price:
            query = query.filter(Restaurant.price <= price)
        results = query.all()
    if category or location or price:
        return render_template('view.html', results=results, location=location,
                               category=category, price=price)
    else:
        results = Restaurant.query.all()
        return render_template('view.html', results=results)

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    results = Restaurant.query.all()
    if request.method == 'POST':
        id = request.form.get('id')
        to_delete = Restaurant.query.get(id)
        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
    return render_template('delete.html', results=results)

@app.route('/update', methods=['POST', 'GET'])
def update():
    results = Restaurant.query.all()
    if request.method == 'POST':
        id = request.form.get('id')
        to_update = Restaurant.query.get(id)
        if to_update:
            to_update.comment=request.form.get('name')
            to_update.grade=request.form.get('location')
            to_update.comment = request.form.get('category')
            to_update.grade = request.form.get('price')
            db.session.commit()
    return render_template('update.html', results = results)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()