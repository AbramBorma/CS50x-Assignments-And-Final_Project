import sqlite3

conn = sqlite3.connect('/home/abram_93/Final_Project/application/explore.db')

cursor = conn.cursor()

with open('/home/abram_93/Final_Project/application/static/files/price_ranges.txt', 'r') as file:
    prices = file.readlines()
    for price in prices:
        cursor.execute('INSERT INTO price (price_range) VALUES (?)', (price.strip(),))
        conn.commit()
conn.close()