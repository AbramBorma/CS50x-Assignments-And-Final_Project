import sqlite3

conn = sqlite3.connect('/home/abram_93/Final_Project/application/explore.db')

cursor = conn.cursor()

categories = ['Dining', 'Nightlife', 'Sightseeing']

for category in categories:
    
    cursor.execute("INSERT INTO category (category) VALUES (?)", (category,))
    
    conn.commit()
conn.close()