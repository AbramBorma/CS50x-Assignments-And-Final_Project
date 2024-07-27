import sqlite3

conn = sqlite3.connect('/home/abram_93/Final_Project/application/explore.db')

cursor = conn.cursor()

categories = ['Dining', 'Nightlife', 'Sightseeing']

# Convert the list to a tuple and use the IN clause
cursor.execute("SELECT id, category FROM category WHERE category IN (?, ?, ?)", tuple(categories))

# Get all matching categories
category_ids = {category: id for id, category in cursor.fetchall()}

subcategories = {'Dining' : ['Restaurant', 'Cafe'],
                 'Nightlife' : ['Bar', 'Pub', 'Nightclub'],
                 'Sightseeing' : ['Historical', 'Museum', 'Park']}

for category, subs in subcategories.items():
    for subcategory in subs:
        # Insert into the subcategory table
        cursor.execute("INSERT INTO subcategory (category_id, subcategory) VALUES (?, ?)", (category_ids[category], subcategory))
        conn.commit()

conn.close()