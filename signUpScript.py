#!/usr/bin/python
print ("Content-type: text/html")
print()
import mysql.connector
import cgi
import cgitb
import ctypes
import json

formData = cgi.FieldStorage()
cgitb.enable()

Email = formData.getvalue("email")
Password = formData.getvalue("password")
FirstName = formData.getvalue("fname")
LastName = formData.getvalue("lname")
Gender = formData.getvalue("gender")

database = mysql.connector.connect(
  host="localhost",
  user="wdsouza",
  passwd="wdsouza177",
  database = "g2"
)
mycursor = database.cursor()
# check if email id exists
sql = f"SELECT * FROM Users WHERE Email_ID = \'{Email}\'"
mycursor.execute(sql)
result = mycursor.fetchone()


if result is None:
    #insert and return success to UI
    mycursor = database.cursor()
    sql = f"INSERT INTO Users (Email_ID,First_Name, Last_Name, Password, Role_ID)VALUES ( \'{Email}\' , \'{FirstName}\' , \'{LastName}\', \'{Password}\' ,1)"
    mycursor.execute(sql)
    #response= "success"
    database.commit()
    database.close()
    result=[]
    rawjson = {"Tag":"success"}
    result.append(rawjson)
    print(json.dumps(result, indent=3))
    
else:
    #return fail to UI
   #response="duplicate"
   #redirectURL = "http://g2.psjconsulting.com/signup.html"
   #print('<html>')
   #print('  <head>')
   #print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
   #print('  </head>')
   #print('</html>')
    
   #ctypes.windll.user32.MessageBoxW(0, "Fail", "Your title", 1)
   result=[]
   rawjson = {"Tag":"fail"}
   result.append(rawjson)
   print(json.dumps(result, indent=3))
