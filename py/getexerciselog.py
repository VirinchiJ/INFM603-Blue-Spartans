#!/usr/bin/python

print ("Content-type: text/html")
print()

import mysql.connector

# import and enable CGI traceback - so errors will show in the browser
import cgitb
cgitb.enable()

database = mysql.connector.connect(
  host="localhost",
  user="tackchen",
  passwd="tackchen831",
  database = "g2"
)
print("""
<form method = "post" action = "displaylog.py">
<select name = \"username\">
""")
mycursor = database.cursor()
sql = "Select * FROM Users"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult :
  print(f"<option>{x[1]} {x[2]}</option>")
print("""
</select>
<input type = \"submit\" value = \"Get the exercise logs\" >
</form>""")
  
