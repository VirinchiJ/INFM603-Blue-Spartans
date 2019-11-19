#!/usr/bin/python

print ("Content-type: text/html\n")

# Create the HTML page title and header for the output
print("""<html xmlns = "http://www.w3.org/1999/xhtml">
   <head>
      <title>Project Form Validation and Database Update</title>
   </head>

   <body style = \"font-family: arial,sans-serif\">""")

# use the Python MySQL connector package
import mysql.connector

# Get the data from the form (through HTTP POST using the Common Gateway Interface)
import cgi
formData = cgi.FieldStorage()

# import and enable CGI traceback - so errors will show in the browser
import cgitb
cgitb.enable()

# For debugging purposes, define the function verboseprint.   It will print out a lot of stuff only if VERBOSE is set to true
VERBOSE = True
def verboseprint(st):
  if VERBOSE:
    print(st)

# Assign Python variables for each of the six form inputs
inputcom = formData.getvalue("inputcom")
logid = formData.getvalue("logid")

# Open the database 
database = mysql.connector.connect(
  host="localhost",
  user="tackchen",
  passwd="tackchen831",
  database = "g2"
)

print(f"""<p>Thank you for entering the new comment.it has been added to the database.
      </p><table border = \"1\" cellpadding = \"3\" cellspacing = \"2\" style = \"background-color: ADD8E6\">
	   <tr>
		 <td>Date</td>
		 <td>User name</td>
		 <td>Exercise Type</td>	
		 <td>Calories</td>
		 <td>Duration</td>
		 <td>Current Weight</td>		 
		 <td>Comment</td>		
	    </tr>""")     

# Now we start running database queries
# Now get the Supervisor ID from the Supervisor name - check to see if supervisor is in the database
mycursor = database.cursor()
sql = f"SELECT * FROM Exercise_Log WHERE Exercise_Log_ID = \'{str(logid)}\'"
mycursor.execute(sql)
myresult = mycursor.fetchone()
useid = myresult[1]
typeid = myresult[2]
cal = myresult[3]
date = myresult[4]
duration = myresult[5]
weight = myresult[6]
trid = 1

sql = f"SELECT Type FROM Exercise_Type WHERE Exercise_Type_ID = \'{typeid}\'"
mycursor.execute(sql)
typeresult = mycursor.fetchone()
typename = typeresult[0]

sql = f"SELECT * FROM Users WHERE User_ID = \'{useid}\'"
mycursor.execute(sql)
uresult = mycursor.fetchone()
firstname = uresult[1]
lastname = uresult[2]

#Check to see if comment is in the database
mycursor = database.cursor()
sql = f"SELECT Comment_ID FROM Comments WHERE Exercise_Log_ID = \'{logid}\'"
mycursor.execute(sql)
myresult = mycursor.fetchone()

# If the employee isn't in the database, add it
if myresult is None:
  verboseprint(f"A new comment is added into database<br>")
  sql = f"INSERT INTO Comments " + "( CommentedBy_ID , Exercise_Log_ID , Comments , Date) "\
  + f"VALUES ( \'{trid}\' , \'{logid}\', \'{inputcom}\',\'GETDATE()\' )"
  verboseprint(f"Comment is already in the database, updating<br>")
  mycursor.execute(sql)
  database.commit()
# else update the comment
else:
  sql = f"UPDATE Comments SET Comments = \'{inputcom}\' WHERE Exercise_Log_ID = \'{logid}\'"
  verboseprint(f"Comment is already in the database, updating<br>")
  mycursor.execute(sql)
  database.commit()

# Now print out each form field's value (helpful for debugging)
print(f"<td>{date}</td>")
print(f"<td>{firstname} {lastname}</td>")
print(f"<td>{typename}</td>")
print(f"<td>{cal}</td>")
print(f"<td>{duration}</td>")
print(f"<td>{weight}</td>")
print(f"<td>{inputcom}</td>")
print("""</tr>
      </table>
      <br/><br/><br/>""")
		
print("""
   </body>
</html>""")
