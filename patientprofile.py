#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Register here"  
print """
<html>
<head>
<style>
#outer
{	
height:100%;
width:100%; 
border:1px solid;
background-image:url("images/4.jpg");
background-repeat:no-repeat;
background-size:cover;
}
#nev
{
height:50px;
width:1340px;
}
#nev ul
{
list-style:none; 
margin-left:10px;
}
#nev ul li
{
float:left;
font-size:35px;
text-align:center;
border:4px solid white;
height:50px;
width:45%;
border-radius:40px;
margin-left:2px;
margin-top:10px ;	
background-color:#00293e;
}
#nev ul li a
{
text-decoration:none;
font-family:calibri;
font-size:30px;
display:block;
color:white;
height:
}
#nev ul li a:hover
{
height:50px;
width:100%;
margin-left:-4px;
margin-top:-4px;
border-radius:10px;
border:4px solid #00293e;
color:#00293e;
text-decoration:none;
background-color:white;
}

</style>
</head>
<body>
<div id="outer">
<div id="nev">
<ul>
  <li> <a href="book.py">Book Appointment<a/></li>
  <li> <a href="myaptpointmen.py">My Appointment<a/></li>
  <li> <a href="changepass.py">Change password<a/></li>
  <li> <a href="logout.py">Logout<a/></li>
  <li> <a href="updateprofile.py">Update profile<a/></li>

  
</ul>
</div>
<table>
"""
import cgi,MySQLdb
e=cgi.fieldStorage().getvalue('id')
#print e
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="select * from tbl_patient where email='"+e+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td>name:</td></tr>",r[1],"</td></tr>"
 print "<tr><td>fathername</td></tr>",r[2],"</td></tr>"
 print "<tr><td>gender</td></tr>",r[3],"</td></tr>"
 print "<tr><td>mobile no</td></tr>",r[4],"</td></tr>"
 print "<tr><td>address</td></tr>",r[5],"</td></tr>"
 print "<tr><td>email</td></tr>",r[6],"</td></tr>"
 print "<tr><td>date</td></tr>",r[8],"</td></tr>"
 print "<tr><td colspan='2' align='center'><a href='edit.py?id="+e+"'>Edit profile</a></td></tr>"
print"""
</div>
</body>
</html>
"""