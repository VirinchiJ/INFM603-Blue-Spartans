#!/usr/bin/python
print ("Content-type: text/html")
print()
import mysql.connector
import cgi
import cgitb
import json
formData = cgi.FieldStorage()
cgitb.enable()
loggedinUserId = 1 #formData.getvalue("id")

database = mysql.connector.connect(
  host="localhost",
  user="wdsouza",
  passwd="wdsouza177",
  database = "g2"
)

mycursor = database.cursor()
# check if email id exists
sql = f"SELECT A.First_Name, U.Age, U.Gender, U.Height, U.Target_Weight FROM Users A\
    join UserDetails U on U.User_ID = A.User_ID Where A.User_ID = \'{loggedinUserId}\'"
mycursor.execute(sql)
rows = mycursor.fetchall()
column = [t[0] for t in mycursor.description]
result = []
for row in rows:
      rowJson = {column[0]: row[0], column[1]: row[1], column[2]: row[2], column[3]: row[3], column[4]: row[4]}
      result.append(rowJson)
print(json.dumps(result, indent=3))
database.close()  
