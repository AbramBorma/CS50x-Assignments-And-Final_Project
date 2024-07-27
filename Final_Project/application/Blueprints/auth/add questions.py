import sqlite3

conn = sqlite3.connect('/home/abram_93/Final_Project/application/explore.db')

cursor = conn.cursor()

with open('/home/abram_93/Final_Project/application/static/files/Questions.txt', 'r') as file:
    questions = file.readlines()
    for question in questions:
        cursor.execute('INSERT INTO questions (question) VALUES (?)', (question.strip(),))
        conn.commit()
conn.close()