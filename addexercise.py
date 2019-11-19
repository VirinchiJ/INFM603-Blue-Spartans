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

# Assign Python variables for each of the 5 form inputs
uid = 1
ipdate = formData.getvalue("ipdate")
ipexercisetype = formData.getvalue("ipexercisetype")  
ipcal = formData.getvalue("ipcal")
ipduration = formData.getvalue("ipduration")
ipweight = formData.getvalue("ipweight")


# Open the database 
database = mysql.connector.connect(
  host="localhost",
  user="tackchen",
  passwd="tackchen831",
  database = "g2"
)

print(f"""<p>Thank you for entering the new exercise log on {ipdate}.It
          has been added to the database.
      </p>
      <strong>The following information has been saved 
          in our database:</strong><br/>
         <table border = \"1\" cellpadding = \"3\" cellspacing = \"2\" style = \"background-color: ADD8E6\">
         <tr>
            <td>Date </td>
            <td>Exercise Type</td>
            <td>Calories</td>
            <td>Duration/Repetitions</td>
            <td>Current Weight(kg)</td>
         </tr>
         <tr>""")
# Now print out each form field's value (helpful for debugging)
print(f"<td>{ipdate}</td>")
print(f"<td>{ipexercisetype}</td>")
print(f"<td>{ipcal}</td>")
print(f"<td>{ipduration}</td>")
print(f"<td>{ipweight}</td>")
print("""</tr>
      </table>
      <br/><br/><br/>""")

# Now we start running database queries
# Now get the Exercise type id from the Exercise type
# Now get the Supervisor ID from the Supervisor name - check to see if supervisor is in the database
mycursor = database.cursor()
sql = f"SELECT Exercise_Type_ID FROM Exercise_Type WHERE Type = \'{ipexercisetype}\' "
mycursor.execute(sql)
myresult = mycursor.fetchone()
exid = myresult[0]

# Add the log to the exercise_log database
verboseprint("Inserting into exercise_log database<br>")
sql = f"INSERT INTO `Exercise_Log` " + "( `User_ID` , `Exercise_Type_ID` , `Calories` , `Date`, `Duration`, `Current_Weight`) "\
+ f"VALUES ( \'{uid}\' , \'{str(exid)}\',\'{ipcal}\', \'{ipdate}\',\'{ipduration}\',\'{ipweight}\')"
verboseprint(f"log insert query is {sql}")
verboseprint("<br>")
try:
  mycursor.execute(sql)
  database.commit()
except mysql.connector.Error as err:
  verboseprint("I caught an error: {}".format(err))
		
print("""
   </body>
</html>""")
