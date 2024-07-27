import sqlite3

conn = sqlite3.connect('/home/abram_93/Final_Project/application/explore.db')

cursor = conn.cursor()

cursor.execute('SELECT id FROM country WHERE country = ?', ('Egypt',))
country_id = cursor.fetchone()[0]

with open('/home/abram_93/Final_Project/application/static/files/Cities.txt', 'r') as file:
    states = file.readlines()
    for state in states:
        cursor.execute('INSERT INTO state (country_id, state) VALUES (?, ?)', (country_id, state.strip(),))
        conn.commit()
conn.close()