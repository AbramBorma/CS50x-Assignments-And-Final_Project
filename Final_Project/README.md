# CairOuting



#### Video Demo: https://youtu.be/bqEHCHdB76k



#### Description:



##### Introduction:

> CairOuting is a Web Application that was created specifically for the purpose of completing CS50x final project. It simply targets all the expats and foreigners that come to Cairo, Egypt for tourism or for a living. This web application main target is provide a full guidance to the expats in the matter of exploring the Hidden Gems of Cairo. I got inspired to create this web application because for example; when you travel to a new country and you try figuring out what to do at that certain country, you directly head to the wonderful and international guide "TripAdvisor", but TripAdvisor mainly shows the mainstream and well know venues and place you should visit at some certain city/country. CairOuting is doing almost the same but from the perspective of the Locals. I have been to both India and Ukraine couple of years ago. I visited some venues recommended by TripAdvisor, but the real fun and experience was through the trips I did with the Locals and the venues recommended by them.



> Thus, I tended to add many venues that the foreigner/expat will get a different experience in Cairo visiting them; Whether these places are Dining, Nightlife or Sightseeing.



> For the sake of completing CS50x final project, I've limited this web application to show venues only in Cairo, but I have Country, State, City and District Models to the database, in order to populate later and can use this web application to be sold to different clients at different cities, states or countries. Also, I have added a feature for the user to Add Venues to the database just for the purpose of CS50x final project, but later I'm going to change the authorities for that feature to be added only by the venue owners when I start selling my web application or rent its services.



##### Requirements:



> pip install flask

> pip install flask-migrate

> pip install flask-session

> pip install sqlalchemy

> pip install flask-sqlalchemy

> pip install python-dotenv



##### Overview:



> CairOuting web application consists of many functions, they are as the following:
>> 1- Homepage: A simple home page showing the categories of venues or in another meaning what the user can do based on the three main categories which are Dining, Nightlife and Sightseeing.

>> 2- What to do?: This tab will show a drop-down menu of the three main categories mentioned above.

>> 3- Venues: In this section, all the venues of different categories and subcategories will be shown to the user in some certain design and paginated. There's a filtration option as well at this section.

>> 4- Add Venue: This section will be responsible for adding new venues to the database and as I mentioned earlier, the user will be allowed to add venues once they are signed in for CS50x final project purpose only.
>> 5- Authentication: This section is for the authentication methods including Registration, Login, Logout and Changing Passwords.



##### Features:



>  ###### 1- Authentication:

>> In authentication there are many sub features which are as following, please note that all the verification are done both in the client and server sides:

>>> A) Registration: In Registration the user has to write a unique username and email. They must write a password between 8-20 characters with at least one lowercase letter, one uppercase letter, one number and one special character. They also must choose a security question and add an answer for it.
>>> B) Login: In Login, the user is required to write their email and password only.
>>> C) Change Password: in Change Password method, the user has to write their email, security question and its correct answer to be able to change the password.
>>> D) Logout: Normal logout method that will clear the session and sign the user out.



>  ##### 2- What to Do?:
>> In this section, the user can navigate from the home page to the three main categories Dining, Nightlife or Sightseeing. He can do either by clicking on the photos in the carousel or by choosing from the drop-down menu of "What to Do?" button. Based on his choice the web application will direct them to the venues of that category.
>  ##### 3- Venues:
>> In Venues section, there are many features:
>>> A) Viewing all the venues in Cairo within the database. The venues in the database contain many essential and useful information of the venue, like:
>>>> I. Name and Description.

>>>> II. Address (District, City, State and Country).

>>>> III. Category and Subcategory.

>>>> IV. Price Range and Photo.

>>>> V. Reviews and Ratings.

>>> B) Adding Reviews and Ratings and the rating will be calculated and showing the floating point out of 5.

>>> C) Filtration: The filtration is done by AJAX requests to the database through the server side. Venues could be filtered by the country, state, city, district, category, subcategory, price range or by all of them combined.



>  ##### 4- Add Venue:

>> In Add Venue section, the logged in user only can add a new venue to the database through out a Form which is verified by client and server sides. After adding a new venue, the user will be directed to the venues page to view all the venues.
I used AJAX requests as well in order for the user to choose states within a certain country, a city within that state, districts in that city and subcategories in the main category.
>> ##### Note: I created tables for countries, states, cities, districts, categories, subcategories and price ranges to be easier to add to them later when I want to populate this web application in different countries, states, etc.. or add to the categories and subcategories.



##### Code:



> The design of code was quite a challenge to me to start using Design Architecture, I googled the different types of architectures and I chose to follow the "3-tiers" Architecture which is consisted of Models, Services and Controllers. I also used a Flask Boilerplate which also included Forms and Blueprints. The directory design was as following:
>>  ##### Application Directory:
>>>This is the main directory of my project. It includes all the Blueprints sub-directories, Static directory, Templates directory, Migration directory, "app.py", "extensions.py", config.py" and the database file. The directories structure is as following:
>>>>  ###### 1- Blueprints:
>>>>> Each Blueprint has the dunder file "__init__.py", "models.py" which has all the models created using SQLAlchemy, "services.py" which has all the logic related to the models, "forms.py" which includes all the validation methods for the forms and finally "controllers.py" for the routes of that Blueprint.
>>>>  ###### 2- Static:
>>>>> This directory has the CSS, JS, Webfonts, Imgs, Venue_images and other used files in the web application.
>>>>  ###### 3- Templates:
>>>>> The templates directory has all the templates within this web application categorized based on the used Blueprints in addition to the "layout.html" templates.
>>>>  ###### 4- Migration:
>>>>> This directory is created using the flask migrate command and it has all the upgraded/downgraded models and their relationships. These models were created using SQLAlchemy ORM.
>>>>  ###### 5- Main Files:
>>>>> The main files are "app.py" which has the Flask Migrate Instances, "config.py" which includes all the configurations such as the session, SQLAlchemy and SECRET_KEY configurations, and the "extensions.py" which includes all the methods and instances that will be recalled and imported in all the other files in the project with without causing the circular dependencies. And lastly, the database file "explore.db" which includes all the models and data saved for the web application.
