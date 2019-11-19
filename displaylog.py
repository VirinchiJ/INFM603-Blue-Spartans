#!/usr/bin/python

print ("Content-type: text/html")
print()
import os
# Get the data from the form
import cgi
formData = cgi.FieldStorage()

# import and enable CGI traceback - so errors will show in the browser
import cgitb
cgitb.enable()
VERBOSE = True
def verboseprint(st):
  if VERBOSE:
    print(st)

querystring = os.environ['QUERY_STRING']
temp=querystring.split('=')
userid=temp[1]

#username = formData.getvalue("username")

import mysql.connector

# open the database - note that we would ordinarily check for errors here
database = mysql.connector.connect(
  host="localhost",
  user="tackchen",
  passwd="tackchen831",
  database = "g2"
)
mycursor = database.cursor()
#sql = f"SELECT User_ID FROM Users WHERE CONCAT(First_Name,\' \',Last_Name) = \'{username}\'"
#mycursor.execute(sql)
#myresult = mycursor.fetchone()
# get next row (only row)
#userid = myresult[0]
# check for error here
# build the table header in HTML (and then we'll print the actual data from Python)
print("""
	  <table border = \"1\" cellpadding = \"3\" cellspacing = \"2\" style = \"background-color: ADD8E6\">
	   <tr>
		 <td>Log ID</td>
		 <td>Date</td>
		 <td>Exercise Type</td>	
		 <td>Calories</td>
		 <td>Duration</td>
		 <td>Current Weight</td>
		 <td>Comment</td>		
	    </tr>""")
sql = f"SELECT * FROM Exercise_Log WHERE User_ID = \'{str(userid)}\'ORDER BY Date ASC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult :
 #next get the information from exercise type table.
   sql = f"SELECT Type FROM Exercise_Type WHERE Exercise_Type_ID = \'{row[2]}\'"
   mycursor.execute(sql)
   typeresult = mycursor.fetchone()
   typename = typeresult[0]
   print( "<tr>")
   print(f"<td>{row[0]}</td><td>{row[4]}</td><td>{typename}</td><td>{row[3]}</td><td>{row[5]}</td><td>{row[6]}</td>")
   sql = f"SELECT Comments FROM Comments WHERE Exercise_Log_ID = \'{row[0]}\'"
   mycursor.execute(sql)
   comresult = mycursor.fetchone()
   if comresult is None:
      print(f"<td>no Comment now</td>")
   else:
      comment = comresult[0]
      print(f"<td>{comment}</td>")
   print("</tr>")
print("</table>")
print("<label>Select a log to leave a comment: </label><br>")

print("""
<form method = "post" action = "addcomment.py">
<select name = \"logid\">
""")
for row in myresult :
   print(f"<option>{row[0]}</option>")
print("""</select><br>Enter the comment:<br><input type=\'text\' name=\'inputcom\'><br>""")
print("""
<input type = \"submit\" value = \"submit\" />
</form>""")




   
