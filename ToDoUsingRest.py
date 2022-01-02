import sqlite3 #import the db file

conn = sqlite3.connect('ToDoUsingRest.db')#create file and connect

#conn.execute('CREATE TABLE IF NOT EXISTS Items (item TEXT, status TEXT, itemDate DATETIME, itemid INTEGER PRIMARY KEY)')#create a table
# conn.execute('CREATE TABLE IF NOT EXISTS users (uname TEXT PRIMARY KEY, pwd TEXT)')#create a table
#print("Created Table Items")
# res="Table created"
cursor = conn.execute("Select * from Items")
for row in cursor:
    print(row[0]," ",row[1]," ", row[2]," ", row[3])
print("Operation select done successfully")