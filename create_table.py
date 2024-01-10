import sqlite3
conn = sqlite3.connect('database.db')
print("connected to database successfully")

conn.execute('CREATE TABLE user (email email, password password,country country,city city,name TEXT, surname TEXT )')
print("created table successfully")

conn.close()