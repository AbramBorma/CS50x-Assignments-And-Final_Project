import sqlite3

conn = sqlite3.connect('/home/abram_93/Final_Project/application/explore.db')

cursor = conn.cursor()

states_cities = {'Cairo': 'Cairo', 'Giza': 'Giza'}

for state, city in states_cities.items():
    cursor.execute("SELECT id FROM state WHERE state = ?", (state,))
    state_id = cursor.fetchone()[0]
    cursor.execute('INSERT INTO city (state_id, city) VALUES (?, ?)', (state_id, city))
    conn.commit()
    
conn.close()