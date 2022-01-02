import sqlite3 #import the db file

conn = sqlite3.connect('ToDoUsingRest.db') #create file and connect

conn.execute('CREATE TABLE IF NOT EXISTS Items (item TEXT, status TEXT, itemDate DATETIME, itemid INTEGER PRIMARY KEY)') #create a table
print("Created Table Items")

cursor = conn.execute("Select * from Items")
for row in cursor:
    print(row[0]," ",row[1]," ", row[2]," ", row[3])
print("Operation select done successfully")
