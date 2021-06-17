#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi, MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
e=cgi.FieldStorage().getvalue('id')
print"""
<html>
<head>
</head>
<body>
<h1>Edit Profile Form </h1>
<hr>
<form action="editcode.py" method="post">
<table>

"""
cur=con.cursor()
query="select * from tbl_patient where email='"+e+"'"
cur.execute(query)
res=cur.fetchall()
for r in res:
 print "<tr><td>name:</td><td><input name='name' value='"+r[1]+"'/></td></tr>"
 print "<tr><td>father name:</td><td><input name='fname' value='"+r[2]+"'/></td></tr>"
 m=""
 fm=""
 if r[3]=="male":
  m="checked"
 if r[3]=="female":
  fm="checked"
 print "<tr><td>gender</td><td><input type='radio' name='gender' value='male' "+m+"/>Male<input type='radio' name='gender' value='female' "+fm+"/>Female</td></tr>"
 print "<tr><td>mobile.no</td><td><input type='number' name='mob' value='"+r[4]+"'/></td></tr>"
 print "<tr><td>email</td><td><input name='email' value='"+r[6]+"' readonly/></td></tr>"
 print "<tr><td>address</td><td><input type='textarea'input name='add' value='"+r[7]+"'/></td></tr>"
 print "<tr><td colspan='3' align='center'><input type='submit' value='update'/></td></tr>"
 
print"""
</table>
</form>
</body>
</html>
"""