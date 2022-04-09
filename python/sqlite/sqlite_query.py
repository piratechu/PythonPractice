import sqlite3

#conn = sqlite3.connect(':memory:')
#connect to database
conn = sqlite3.connect("myData.db")

#create a cursor
cursor = conn.cursor()

#drop table command
sql = "drop table student"
#sql = "select * from student where gender = 'M'"
# query a table
cursor.execute(sql)

#items = cursor.fetchall()
#print(cursor.fetchone())
#print(cursor.fetchmany(3))
#first record , column
#print(cursor.fetchone()[1]) 
#print("ID \t\t Name \t\t Gender")
#print("===== \t\t ===== \t\t =====")
#for item in items:
#    print(item[0] , "\t\t" , item[1] , "\t\t" , item[2])


#close our cursor and connection
cursor.close()
conn.commit
conn.close
