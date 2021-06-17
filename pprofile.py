#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<link href="css/pprofile.css" rel="stylesheet" type="text/css"/>
<script src="js/index.js">
</script>
</head>
<body onload="slide()">
<div id="outer">
<div id="header">
   <div id="logo">
    <img src="images/logo.jpg" height="150px" width="150px" />
   </div>
   <div id="heading">
   
<p align="center" style="font-size:50px;"><b>Sanjay Gandhi PostGraduate of Medical Science</b></p>

</div><br/>
</br>
   
</br><div id="menu">
<ul>
<li><a href="book.py">Book appointment</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="myappointment.py">My appointmentment</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="Changepass.py">Change Password</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="logout.py">Logout</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="patcode.py">Update Profile</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


</ul>
</div>
<br/>
<br/>
 <div id="slider">
 <h1>Patientn Profile-:<h1>
<table>
"""
import cgi,MySQLdb
e=cgi.FieldStorage().getvalue('id')
print e
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="select * from tbl_patient where email='"+e+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td>Name :</td><td>",r[1],"</td></tr>"
 print "<tr><td>Father Name :</td><td>",r[2],"</td></tr>"
 print "<tr><td>Gender No :</td><td>",r[3],"</td></tr>"
 print "<tr><td>Mobile No :</td><td>",r[4],"</td></tr>"
 print "<tr><td>Address :</td><td>",r[5],"</td></tr>"
 print "<tr><td>Email :</td><td>",r[6],"</td></tr>"
 print "<tr><td>Reg.Date :</td><td>",r[8],"</td></tr>"
 print "<tr><td colspan='2' align='center'><a href='edit.py?id="+e+"'>Edit Profile</a></td></tr>"
 print """
	 </table>
    </div><br/>
	
	<div id="footer">
	<div id="f1"><center><font id="ss">Created By--</font><br/><br/><br/>Shikha sahu <br/>Copyrite &copy 2019-20</center>
	   
	
	</div>
	
	
	<div id="f2"><center><font id="ss">About Us--</font></center><br/><p>Sanjay Gandhi Postgraduate Institute of Medical Science(SGPGIMS)
	-<br/>It is a medical Institute under State Legislature Act,located in lucknow,Uttar Pradesh.It was establlished in 1983 and is
	named after <i>Sanjay Gandhi.</i>The institute is on a 550 acres residental campus at Raebareli road,15km from the main city.The
	institute offers its own degrees,which are recognised by the Medical Council of India</p><br/></div>
	<div id="f3">
	<font id="ss"><center>Contact US-</center></font><br/>
	<font color="white">Email.Id--shikhasahu</font><br/>
	<font color="white">Mobile.No-9161626010</font><br/><br/>
	<img id="in" src="images/twitter.png" height="50px" width="50px"/>twitter<br/>
	<img id="in" src="images/facebook.png" height="50px" width="50px"/>facebook<br/>
	<img id="in" src="images/instagram.png" height="50px" width="50px"/>instagram<br/>
	<img id="in" src="images/google-plus.png" height="50px" width="50px"/>google
	</div>
	</div>
</div>
</body>
</html>
"""
