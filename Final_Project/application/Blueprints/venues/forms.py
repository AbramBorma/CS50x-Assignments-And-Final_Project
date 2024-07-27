''' Creating the Validator Class to validate the Add_Venue form.'''

class Validator:
    
    @staticmethod
    def venue_country(country_id):
        if not country_id:
            return 'Please select a valid country from the list'
        return None
    
    @staticmethod
    def venue_state(state_id):
        if not state_id:
            return 'Please select a valid state from the list'
        return None
    
    @staticmethod
    def venue_city(city_id):
        if not city_id:
            return 'Please select a valid city from the list'
        return None
    
    @staticmethod
    def venue_district(district_id):
        if not district_id:
            return 'Please select a valid district from the list'
        return None
    
    @staticmethod
    def venue_category(category_id):
        if not category_id:
            return 'Please select a valid category from the list'
        return None
    
    @staticmethod
    def venue_subcategory(subcategory_id):
        
        if not subcategory_id:
            return 'Please select a valid subcategory from the list'
        return None
    
    @staticmethod
    def venue_description(description):
        
        if not description:
            return 'Please write a description for the venue'
        
        elif len(description) < 30 or len(description) > 500:
            return 'The description should be between 50 & 500 letters'
        
        return None
    
    @staticmethod
    def venue_price_range(price_range_id):
        
        if not price_range_id:
            return 'Please select a valid price range from the list'
        return None
    
    @staticmethod
    def venue_location(location):
        if not location:
            return 'Please enter a location'
        return None
    
    @staticmethod
    def venue_review(review):
        if len(review) > 500:
            return "The maximum review length should be less than 500 letters"
        return None
    
    @staticmethod
    def venue_rating(rating):
        if not rating:
            return "Please select a rating"
        return None
    