import sqlite3

#conn = sqlite3.connect(':memory:')
#connect to database
conn = sqlite3.connect("myData.db")

#create a cursor
cursor = conn.cursor()

# insert a table
#sql = '''INSERT INTO student( '2', 'Mary', 'F')'''

# insert into many record
many_students = [
                ('John','M'),
                ('Mary','F'),
                ('Brown','M'),
                ('Kuewa','M'),
                ('Paris','F'),
                ('Kenny','M')
                ]
#sql = "INSERT INTO student values (?,?,?)"
cursor.executemany("INSERT INTO student (name,gender) values (?,?)",many_students)

#commit our command
#cursor.commit()

#close our cursor and connection
cursor.close()
conn.commit()
conn.close()
