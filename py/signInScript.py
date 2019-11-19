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
# check if email id exists in users table
sql = f"SELECT User_ID, Role_ID FROM Users WHERE Email_ID = \'{Email}\' and Password= \'{Password}\'"
mycursor.execute(sql)
resultUser = mycursor.fetchone()

mycursor = database.cursor()
#check if email id exists in trainers table
sql = f"SELECT Trainer_ID, Role_ID FROM Trainers WHERE Email_ID = \'{Email}\' and Password= \'{Password}\'"
mycursor.execute(sql)
resultTrainer = mycursor.fetchone()

if resultUser is not None:
 result=[]
 userid= resultUser[0]
 roleid = resultUser[1]
 rawjson = {"Tag":"success","UserId":userid,"RoleId":roleid}
 result.append(rawjson)
 print(json.dumps(result, indent=3))
 database.close()
elif resultTrainer is not None:
 result=[]
 userid= resultTrainer[0]
 roleid = resultTrainer[1]
 rawjson = {"Tag":"success","UserId":userid,"RoleId":roleid}
 result.append(rawjson)
 print(json.dumps(result, indent=3))
 database.close()
else:
#return fail to UI
    result=[]
    rawjson = {"Tag":"fail"}
    result.append(rawjson)
    print(json.dumps(result, indent=3))
