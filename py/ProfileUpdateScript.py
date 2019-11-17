#!/usr/bin/python
print ("Content-type: text/html")
print()
import mysql.connector
import cgi
import cgitb
formData = cgi.FieldStorage()
cgitb.enable()
loggedinUserId = 1 #formData.getvalue("id")

Name = formData.getvalue("name")
Age = formData.getvalue("age")
Gender = formData.getvalue("gender")
Height = formData.getvalue("height")
Weight = formData.getvalue("weight")

database = mysql.connector.connect(
  host="localhost",
  user="wdsouza",
  passwd="wdsouza177",
  database = "g2"
)
mycursor = database.cursor()
sql = f"Update UserDetails \
Set Age =\'{Age}\',Gender=\'{Gender}\',Height=\'{Height}\', Target_Weight= \'{Weight}\'\
Where User_ID = \'{loggedinUserId}\'"
mycursor.execute(sql)
database.commit()

sql = f"Update Users \
Set First_Name =\'{Name}\'\
Where User_ID = \'{loggedinUserId}\'"
mycursor.execute(sql)
database.commit()