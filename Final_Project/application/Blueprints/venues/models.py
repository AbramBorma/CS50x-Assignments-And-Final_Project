from application.extensions import db
from sqlalchemy import ForeignKey

''' Creating all the models in the database.
    Only the serialize method were recommended by Microsoft Copilot '''

class Country(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(64), unique=True, nullable=False)
    states = db.relationship('State', backref='country', lazy=True)
    
    def serialize(self):
        return {
            'id' : self.id,
            'country' : self.country
        }
    
class State(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, ForeignKey('country.id'))
    state = db.Column(db.String(64), unique=True, nullable=False)
    cities = db.relationship('City', backref='state', lazy=True)
    
    def serialize(self):
        return {
            'id' : self.id,
            'state' : self.state
        }
    
class City(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    state_id = db.Column(db.Integer, ForeignKey('state.id'))
    city = db.Column(db.String(64), unique=True, nullable=False)
    districts = db.relationship('District', backref='city', lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'city': self.city
        }
    
class District(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, ForeignKey('city.id'))
    district = db.Column(db.String(64), unique=True, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'district': self.district
        }
    
class Category(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), unique=True, nullable=False)
    subcategories = db.relationship('Subcategory', backref='category', lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'category': self.category
        }
    
class Subcategory(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, ForeignKey('category.id'))
    subcategory = db.Column(db.String(64), unique=True, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'subcategory': self.subcategory
        }

class Price(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    price_range = db.Column(db.String(64), unique=True, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'price_range': self.price_range
        }
    
class Venue(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, ForeignKey('country.id'), nullable=False)
    country = db.relationship('Country', backref='venues')
    state_id = db.Column(db.Integer, ForeignKey('state.id'), nullable=False)
    state = db.relationship('State', backref='venues')
    city_id = db.Column(db.Integer, ForeignKey('city.id'), nullable=False)
    city = db.relationship('City', backref='venues')
    district_id = db.Column(db.Integer, ForeignKey('district.id'), nullable=False)
    district = db.relationship('District', backref='venues')
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='venues')
    subcategory_id = db.Column(db.Integer, ForeignKey('subcategory.id'), nullable=False)
    subcategory = db.relationship('Subcategory', backref='venues')
    price_range_id = db.Column(db.Integer, ForeignKey('price.id'), nullable=False)
    price_range = db.relationship('Price', backref='venues')
    image_path = db.Column(db.String(256), unique=True, nullable=False)
    reviews = db.relationship('Review', backref='venue', lazy=True)
    ratings = db.relationship('Rating', backref='venue', lazy=True)
    
    def serialize(self):
        return {
            'id' : self.id,
            'name': self.name,
            'description': self.description,
            'country': self.country.country,
            'state': self.state.state,
            'city': self.city.city,
            'district': self.district.district,
            'category': self.category.category,
            'subcategory': self.subcategory.subcategory,
            'price_range': self.price_range.price_range,
            'image_path': self.image_path,
            'reviews' : self.reviews,
            'ratings' : self.ratings
        }
        
class Review(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text)
    venue_id = db.Column(db.Integer, ForeignKey('venue.id'))
    
class Rating(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    venue_id = db.Column(db.Integer, ForeignKey('venue.id'))