import sqlite3

conn = sqlite3.connect('/home/abram_93/Final_Project/application/explore.db')

cursor = conn.cursor()

cursor.execute('SELECT id FROM city WHERE city = ?', ('Cairo',))
city_id = cursor.fetchone()[0]

with open('/home/abram_93/Final_Project/application/static/files/Cairo_Districts.txt', 'r') as file:
    districts = file.readlines()
    for district in districts:
        cursor.execute('INSERT INTO district (city_id, district) VALUES (?, ?)', (city_id, district.strip(),))
        conn.commit()
conn.close()