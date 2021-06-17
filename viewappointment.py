#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="select * from tbl_appointment"
cur.execute(q)
res=cur.fetchall()
print """
<html>
<head>
<link href="css/viewappointment.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div id="outer">
<div id="header">
   <div id="logo">
    <img src="images/logo.jpg" height="150px" width="150px" />
   </div>
   <div id="heading">
   
<p align="center" style="font-size:50px;"><b>Sanjay Gandhi PostGraduate of Medical Science</b></p>
</div><br/>
</br>
<div id="menu">
<ul>
<li><a href="book.py">Book-Appointment</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="myappointment.py"></a>My-Appointment</li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="changepass.py">Change-Password</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="logout.py">Logout</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="update.py">Update-profile</a></li>
<input type="text" placeholder="search"/>
</ul>
</div>
<br/>
<br/>
   <div id="slider">
  <form action="dcpcode.py" method="post"><center>
  <h1><font color="white">View-Appointment</font></h1>
  <font color="white">
<table>
</form>
<tr>
<th>App.ID</th>
<th>Doc.ID</th>
<th>Patient Name</th>
<th>DOA</th>
<th>Post Date</th>
<th>Status</th>
<th>Update Status</th>
</tr>
"""
for r in res:
 print "<tr>"
 print "<td>",r[0],"</td>"
 print "<td>",r[1],"</td>"
 print "<td>",r[2],"</td>"
 print "<td>",r[3],"</td>"
 print "<td>",r[4],"</td>"
 print "<td>",r[5],"</td>"
 print "<td><a href='ups.py?id="+str(r[0])+"&s="+str(r[5])+"'>Update Status</a></td>"
 print "</tr>"


print """
</form>
</table>
	</div>
	<br/>
	<div id="footer">
	<div id="f1"><center><h3>Created By--</h3><br/>Shikha sahu <br/>Copyrite &copy</center>
	   
	
	</div>
	
	
	<div id="f2"><center><h3>About Us--</h3></center><br/><p>Sanjay Gandhi Postgraduate Institute of Medical Science(SGPGIMS)
	-<br/>It is a medical Institute under State Legislature Act,located in lucknow,Uttar Pradesh.It was establlished in 1983 and is
	named after <i>Sanjay Gandhi.</i>The institute is on a 550 acres residental campus at Raebareli road,15km from the main city.The
	institute offers its own degrees,which are recognised by the Medical Council of India</p><br/></div>
	<div id="f3">
	<h3><center>Contact US-</center></h3><br/>
	<img id="tw" src="images/twitter.png" height="50px" width="50px"/>twitter
	<img id="in" src="images/facebook.png" height="50px" width="50px"/>facebook<br/>
	<img id="tw" src="images/instagram.png" height="50px" width="50px"/>instagram
	<img id="in" src="images/google-plus.png" height="50px" width="50px"/>google
	</div>
	</div>
</div>
</body>
</html>
"""