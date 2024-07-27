import sqlite3

conn = sqlite3.connect('/home/abram_93/Final_Project/application/explore.db')

cursor = conn.cursor()

with open('/home/abram_93/Final_Project/application/static/files/Countries.txt', 'r') as file:
    countries = file.readlines()
    for country in countries:
        cursor.execute('INSERT INTO country (country) VALUES (?)', (country.strip(),))
        conn.commit()
conn.close()