import sqlite3

#conn = sqlite3.connect(':memory:')
#connect to database
conn = sqlite3.connect("myData.db")

#create a cursor
cursor = conn.cursor()

#create a table
sql = "Create table student( ID INTEGER PRIMARY KEY  AUTOINCREMENT, name text, gender text)"
# datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

cursor.execute(sql)

#close our cursor and connection
cursor.close()
conn.commit
conn.close
