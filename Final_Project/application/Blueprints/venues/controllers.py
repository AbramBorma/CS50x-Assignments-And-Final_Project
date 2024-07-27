from flask import request, render_template, redirect, jsonify, Blueprint, flash, session
from werkzeug.utils import secure_filename
import os
from application.extensions import login_required
from application.Blueprints.venues.services import AddVenue, getVenue, venueRevRating
from .forms import Validator
from math import ceil


venue = Blueprint('venue', __name__, template_folder="templates/venues")

PROJECT_DIR = '/workspaces/57132653/project'
UPLOAD_FOLDER = os.path.join(PROJECT_DIR, 'application/static/venue_imgs/')

@venue.route("/add_venue", methods=['GET', 'POST'])
@login_required
def add_venue():

    countries = AddVenue.get_countries()
    states = AddVenue.get_states_by_country(country_id=None)
    cities = AddVenue.get_cities_by_state(state_id=None)
    districts = AddVenue.get_districts_by_city(city_id=None)
    categories = AddVenue.get_categories()
    subcategories = AddVenue.get_subcategories_by_category(category_id=None)
    prices = AddVenue.get_price_ranges()

    if request.method == 'POST':
        if request.is_json:

            country_id = request.get_json().get('countryId')
            state_id = request.get_json().get('stateId')
            city_id = request.get_json().get('cityId')
            category_id = request.get_json().get('categoryId')

            states = AddVenue.get_states_by_country(country_id)
            cities = AddVenue.get_cities_by_state(state_id)
            districts = AddVenue.get_districts_by_city(city_id)
            subcategories = AddVenue.get_subcategories_by_category(category_id)

            data = {
                'states': [state.serialize() for state in states],
                'cities': [city.serialize() for city in cities],
                'districts': [district.serialize() for district in districts],
                'subcategories': [subcategory.serialize() for subcategory in subcategories]
            }
            return jsonify(data)

        else:
                # If there are no errors, handle the form submission
                # ... handle form submission ...
                country_id = request.form.get('country_id')
                state_id = request.form.get('state_id')
                city_id = request.form.get('city_id')
                district_id = request.form.get('district_id')
                category_id = request.form.get('category_id')
                subcategory_id=request.form.get('subcategory_id')
                name = request.form.get('name')
                description = request.form.get('description')
                price_range_id = request.form.get('price_range_id')

                image_path = request.files['image_path']
                filename = secure_filename(image_path.filename)
                image_path.save(os.path.join(UPLOAD_FOLDER, filename))
                image_path = os.path.join(UPLOAD_FOLDER, filename)  # Construct the image file path

                review = request.form.get('review')
                rating = request.form.get('rating')
                # This is a form submission

                errors = []
                validators = {
                'country_id': Validator.venue_country,
                'state_id': Validator.venue_state,
                'city_id': Validator.venue_city,
                'district_id': Validator.venue_district,
                'category_id': Validator.venue_category,
                'subcategory_id': Validator.venue_subcategory,
                'description': Validator.venue_description,
                'price_range_id': Validator.venue_price_range,
                'review': Validator.venue_review,
                'rating': Validator.venue_rating
                # 'image_path': Validator.venue_image_path
                }

                for field, validator in validators.items():
                    error = validator(request.form.get(field))
                    if error is not None:
                        errors.append(error)
                if errors:
                    # If there are errors, re-render the form with the errors
                    print(errors)
                    return render_template("venues/add_venue.html", errors=errors)
                else:
                    AddVenue.add_venue(country_id=country_id,
                                   state_id=state_id,
                                   city_id=city_id,
                                   district_id=district_id,
                                   category_id=category_id,
                                   subcategory_id=subcategory_id,
                                   name=name,
                                   description=description,
                                   price_range_id=price_range_id,
                                   image_path=image_path,
                                   review=review,
                                   rating=rating)
                    return redirect('/venues')

    return render_template("venues/add_venue.html", countries=countries,
                                                    states=states,
                                                    cities=cities,
                                                    districts=districts,
                                                    categories=categories,
                                                    subcategories=subcategories,
                                                    prices=prices,
                                                    custom_js="addVenue",
                                                    custom_css="auth")



@venue.route("/<category>", methods=["GET", "POST"])
def show_category(category):

    category = category.capitalize()

    page = request.args.get('page', 1, type=int)
    per_page = 5
    all_venues = getVenue.get_venues_by_category(category)

    start = (page - 1) * per_page
    end = start + per_page

    venues = all_venues[start:end]

    # This is the path to your static directory
    static_dir = '/workspaces/57132653/project/application/static/'

    # Iterate over each venue and get the relative path for each image
    for venue in venues:
        # This is the absolute path that you get from the database
        absolute_path = venue['image_path']

        # Use os.path.relpath() to get the relative path
        venue['relative_path'] = os.path.relpath(absolute_path, static_dir)  # And this line

        venue_id = venue['id']
        venue['reviews'] = getVenue.get_reviews(venue_id)
        venue['average_ratings'] = getVenue.get_average_ratings(venue_id)

    if not venues:
        flash("There are no venues in this section")

    total_pages = ceil(len(all_venues)/per_page)

    pagination = {
        'page': page,
        'per_page': per_page,
        'total_pages': total_pages,
        'has_prev': page > 1,
        'has_next': page < total_pages,
        'prev_num': page - 1 if page > 1 else None,
        'next_num': page + 1 if page < total_pages else None,
    }
    return render_template(f"venues/{category.lower()}.html", venues=venues, pagination=pagination, custom_css="venue")

@venue.route("/venues", methods=['GET', 'POST'])
def show_venues():

    countries = AddVenue.get_countries()
    states = AddVenue.get_states_by_country(country_id=None)
    cities = AddVenue.get_cities_by_state(state_id=None)
    districts = AddVenue.get_districts_by_city(city_id=None)
    categories = AddVenue.get_categories()
    subcategories = AddVenue.get_subcategories_by_category(category_id=None)
    prices = AddVenue.get_price_ranges()

    def process_venues(all_venues, page, per_page=5):
        start = (page - 1) * per_page
        end = start + per_page
        venues = all_venues[start:end]

        static_dir = '/workspaces/57132653/project/application/static/'

        for venue in venues:
            absolute_path = venue['image_path']
            venue['relative_path'] = os.path.relpath(absolute_path, static_dir)
            venue_id = venue['id']
            venue['reviews'] = getVenue.get_reviews(venue_id)
            venue['average_ratings'] = getVenue.get_average_ratings(venue_id)

        if not venues:
            flash("There are no venues")

        total_pages = ceil(len(all_venues) / per_page)

        pagination = {
            'page': page,
            'per_page': per_page,
            'total_pages': total_pages,
            'has_prev': page > 1,
            'has_next': page < total_pages,
            'prev_num': page - 1 if page > 1 else None,
            'next_num': page + 1 if page < total_pages else None,
        }

        return render_template("venues/venues.html", venues=venues,
                               countries=countries,
                               states=states,
                               cities=cities,
                               districts=districts,
                               categories=categories,
                               subcategories=subcategories,
                               prices=prices,
                               custom_js="filterVenue",
                               custom_css="venue",
                               pagination=pagination)

    def filter_venues(filters, page=1):
        filtered_venues = getVenue.filter_venues(filters)
        return filtered_venues

    if request.method == 'POST':
        if request.is_json:
            country_id = request.get_json().get('countryId')
            state_id = request.get_json().get('stateId')
            city_id = request.get_json().get('cityId')
            category_id = request.get_json().get('categoryId')

            states = AddVenue.get_states_by_country(country_id)
            cities = AddVenue.get_cities_by_state(state_id)
            districts = AddVenue.get_districts_by_city(city_id)
            subcategories = AddVenue.get_subcategories_by_category(category_id)

            data = {
                'states': [state.serialize() for state in states],
                'cities': [city.serialize() for city in cities],
                'districts': [district.serialize() for district in districts],
                'subcategories': [subcategory.serialize() for subcategory in subcategories]
            }
            return jsonify(data)

        else:
            filters = {
                'country_id': request.form.get('country_id'),
                'state_id': request.form.get('state_id'),
                'city_id': request.form.get('city_id'),
                'district_id': request.form.get('district_id'),
                'category_id': request.form.get('category_id'),
                'subcategory_id': request.form.get('subcategory_id'),
                'price_range_id': request.form.get('price_range_id'),
            }

            session['filters'] = filters  # Store filters in session

            all_venues = filter_venues(filters)
            return process_venues(all_venues, page=1)

    else:
        page = request.args.get('page', 1, type=int)
        filters = session.get('filters')
        if filters:
            filtered_venues = filter_venues(filters, page=page)
            return process_venues(filtered_venues, page=page)
        else:
            all_venues = getVenue.get_all_venues()
            return process_venues(all_venues, page=page)


@venue.route("/add_review", methods=['POST'])
def add_review_rating():
    venue_id = request.form.get("venue_id")
    rating = request.form.get("rating")
    review = request.form.get("review")

    venueRevRating.add_rating(venue_id, rating)

    if review.strip():  # Check if review text is not empty or contains only whitespace
        venueRevRating.add_review(venue_id, review)

    return redirect('/venues')
