#!/usr/bin/python
print ("Content-type: text/html")
print()
import mysql.connector
import cgi
import cgitb
import json

cgitb.enable()
import os
formData = cgi.FieldStorage()
# For debugging purposes, define the function verboseprint.   It will print out a lot of stuff only if VERBOSE is set to true
VERBOSE = True
def verboseprint(st):
  if VERBOSE:
    print(st)


#querystring = os.environ['QUERY_STRING']
#temp=querystring.split('=')
#trainer=temp[1]
trainer=formData.getvalue("userId")
#verboseprint(f"New Trainer ID is {querystring}")
#verboseprint(f"New t ID is {trainer}")

database = mysql.connector.connect(
  host="localhost",
  user="anuja09",
  passwd="anuja09325",
  database = "g2"
)

mycursor = database.cursor()
mycursor.execute("Select User_ID,First_Name,Last_Name FROM Users where Trainer_ID =%s", (trainer,))
rows = mycursor.fetchall()
column = [t[0] for t in mycursor.description]
result = []
for row in rows:
      rowJson = {column[0]: row[0], column[1]: row[1], column[2]: row[2]}
      result.append(rowJson)
print(json.dumps(result, indent=3))
database.close()  
