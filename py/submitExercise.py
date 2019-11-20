#!/usr/bin/python

print ("Content-type: text/html")
print()

import mysql.connector

# Get the data from the form (through HTTP POST using the Common Gateway Interface)
import cgi
formData = cgi.FieldStorage()

# import and enable CGI traceback - so errors will show in the browser
import cgitb
cgitb.enable()

database = mysql.connector.connect(
  host="localhost",
  user="tackchen",
  passwd="tackchen831",
  database = "g2"
)
mycursor = database.cursor()
print("""
<form method = "post" action = "./addexercise.py"><table class="table table-striped">
<thead class="thead-light"><tr><th>Date</th><th>Exercise</th><th>Calories</th><th>Duration/Repetitions</th><th>Current Weight(lbs)</th></tr></thead>
<tbody><tr>
<td><input type= "date" name= \"ipdate\"></td>
<td><select name = \"ipexercisetype\">
""")
sql = "Select * FROM Exercise_Type"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult :
  print(f"<option>{x[1]}</option>")
print("""
</td>
<td><input type = "number" name = \"ipcal\"></td>
<td><input type = "number" name = \"ipduration\"></td>
<td><input type = "number" name = \"ipweight\"></td></tr></tbody><br><br>
</table><input type = \"submit\" value = \"Submit\" /></form>""")
  
