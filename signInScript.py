#!/usr/bin/python
print ("Content-type: text/html")
print()
import mysql.connector
import cgi
import cgitb
import json

formData = cgi.FieldStorage()
cgitb.enable()

Email = formData.getvalue("inputEmail")
Password = formData.getvalue("inputPassword")

database = mysql.connector.connect(
  host="localhost",
  user="wdsouza",
  passwd="wdsouza177",
  database = "g2"
)

mycursor = database.cursor()
# check if email id exists
sql = f"SELECT User_ID FROM Users WHERE Email_ID = \'{Email}\' and Password= \'{Password}\'"
mycursor.execute(sql)
result = mycursor.fetchone()

if result is not None:
    result=[]
    rawjson = {"Tag":"success","id":Email,"pass":Password}
    result.append(rawjson)
    print(json.dumps(result, indent=3))
    database.close()
else:
    #return fail to UI
    result=[]
    rawjson = {"Tag":"fail","id":Email,"pass":Password}
    result.append(rawjson)
    print(json.dumps(result, indent=3))