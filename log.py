#!/usr/bin/python

print ("Content-type: text/html\n")

print("""<html xmlns = "http://www.w3.org/1999/xhtml">
   <head>
   </head>
   <body style = \"font-family: arial,sans-serif\">""")

import mysql.connector
import cgi
import cgitb
cgitb.enable()


requestData = cgi.FieldStorage()

logdate = requestData.getvalue("date")
uid = requestData.getvalue("uid")

database = mysql.connector.connect(
  host="localhost",
  user="tackchen",
  passwd="tackchen831",
  database = "g2"
)

print("The date you selected is :"+logdate)
print(f"""<p>Here are the exercise logs.
      </p>      
         <table border = \"1\" cellpadding = \"3\" cellspacing = \"2\" style = \"background-color: ADD8E6\">
         <tr>
            <td>Exercise Type </td>
            <td>Calories </td>
            <td>Duration</td>
            <td>Current Weight</td>
            <td>Comment</td>
            </tr>
         <tr>""")
mycursor = database.cursor()
sql = f"SELECT Exercise_Log_ID, Exercise_Type_ID, Calories, Duration, Current_Weight FROM Exercise_Log WHERE User_ID = \'{str(uid)}\' AND Date = STR_TO_DATE(\'{str(logdate)}\', \'%Y%m%d\')"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult :
    sql = f"SELECT Type FROM Exercise_Type WHERE Exercise_Type_ID = \'{row[1]}\'"
    mycursor.execute(sql)
    typeresult = mycursor.fetchone()
    typename = typeresult[0]
    print( "<tr>")
    print(f"<td>{typename}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td>")
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

print("</body>")
