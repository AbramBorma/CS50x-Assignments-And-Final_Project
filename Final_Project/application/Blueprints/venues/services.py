from application.extensions import db
from application.Blueprints.venues.models import Venue, Country, State, City, District, Category, Subcategory, Price, Review, Rating
from sqlalchemy import func

''' Creating AddVenue Class and its static methods to retrieve the data being used
    with AJAX requests and to add the new venues to the database '''

class AddVenue:
    
    @staticmethod
    def add_venue(country_id, state_id, city_id, district_id, name, description, category_id, subcategory_id, price_range_id, image_path, review, rating):
        
        venue = Venue(country_id=country_id,
                      state_id=state_id,
                      city_id=city_id,
                      district_id=district_id,
                      name=name,
                      description=description,
                      category_id=category_id,
                      subcategory_id=subcategory_id,
                      price_range_id=price_range_id,
                      image_path=image_path)
        db.session.add(venue)
        db.session.flush()
        
        review = Review(review=review, venue_id=venue.id)
        db.session.add(review)
        
        rating = Rating(rating=rating, venue_id=venue.id)
        db.session.add(rating)
        
        db.session.commit()
        
    @staticmethod
    def get_countries():
        return Country.query.all()
    
    @staticmethod
    def get_states_by_country(country_id):
        return State.query.filter_by(country_id=country_id).all()
    
    @staticmethod
    def get_cities_by_state(state_id):
        return City.query.filter_by(state_id=state_id).all()
    
    @staticmethod
    def get_districts_by_city(city_id):
        return District.query.filter_by(city_id=city_id).all()
    
    @staticmethod
    def get_categories():
        return Category.query.all()
    
    @staticmethod
    def get_subcategories_by_category(category_id):
        return Subcategory.query.filter_by(category_id=category_id).all()
    
    @staticmethod
    def get_price_ranges():
        return Price.query.all()

''' Creating getVenue Class and its static methods to retrieve the data being used
    with AJAX requests for filtration and to retrieve the venues from the database '''

class getVenue:
    
    @staticmethod
    def get_average_ratings(venue_id):
        
        # The below line of code were written with the help of ChatGPT.
        average_ratings = db.session.query(func.avg(Rating.rating)).filter(Rating.venue_id == venue_id).scalar()
        return round(average_ratings or 0, 2)
    
    def get_reviews(venue_id):
        reviews = db.session.query(Review.review).filter(Review.venue_id == venue_id).all()
        if not reviews:
            return None
        return [review[0] for review in reviews]
        
    @staticmethod
    def get_all_venues():
        venues =  Venue.query.all()
        if not venues:
            return "There are no venues"
        return [venue.serialize() for venue in venues]
    
    @staticmethod
    def get_venues_by_category(category_name):
        category = Category.query.filter_by(category=category_name).first()
        if category is None:
            return f"There is no '{category_name}' Category"
        venues = Venue.query.filter_by(category=category).all()
        if not venues:
            return f"There are no venues in the '{category_name}' Section"
        return [venue.serialize() for venue in venues]
    

    @staticmethod
    def filter_venues(filters):
        query = Venue.query

        if filters.get('country_id'):
            query = query.filter_by(country_id=filters['country_id'])
        if filters.get('state_id'):
            query = query.filter_by(state_id=filters['state_id'])
        if filters.get('city_id'):
            query = query.filter_by(city_id=filters['city_id'])
        if filters.get('district_id'):
            query = query.filter_by(district_id=filters['district_id'])
        if filters.get('category_id'):
            query = query.filter_by(category_id=filters['category_id'])
        if filters.get('subcategory_id'):
            query = query.filter_by(subcategory_id=filters['subcategory_id'])
        if filters.get('price_range_id'):
            query = query.filter_by(price_range_id=filters['price_range_id'])
        
        venues = query.all()
        return [venue.serialize() for venue in venues]

# The below class is to allow the user to add reviews and rating to the venue.
class venueRevRating:
    @staticmethod
    def add_review(venue_id, review):
        review = Review(review=review, venue_id=venue_id)
        db.session.add(review)
        db.session.commit()
    
    @staticmethod    
    def add_rating(venue_id, rating):
        rating = Rating(rating=rating, venue_id=venue_id)
        db.session.add(rating)
        db.session.commit()