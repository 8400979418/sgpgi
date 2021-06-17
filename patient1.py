#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<link href="css/doctor1.css" rel="stylesheet" type="text/css"/>
<head>
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
<li><a href="index.html">Home</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="about.py">About us</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="doctor1.py">Doctor</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="patient1.py">Patient</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="login.py">Login</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<li><a href="contact.py">Contact us</a></li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<input type="text" placeholder="search"/>
</ul>
</div>
<br/>
<br/>
   <div style="height:500px;">
   <form action="patcode.py" method="post">
   <center>
   <h1>Patient Registraton</h1>
   <table>
   <tr>
   <td>Name</td>
   <td><input type="text" name="name"/></td>
   </tr>
   <tr>
   <td>F'name</td>
   <td><input type="text" name="fname"/></td>
   </tr>
   <tr>
   <td>Gender</td>
   <td><input type="radio" name="a" value="male"/>Male
   <td><input type="radio" name="a" value="female"/>Female
   </td>
   </tr>
   <tr>
   <td>Email</td>
   <td><input type="email" name="email"/></td>
   </tr>
   <tr>
   <td>Password</td>
   <td><input type="password" name="password"/></td>
   </tr>
   <tr>
   <td>Mobile</td>
   <td><input type="text" name="mobile"/></td>
   </tr>
   <tr>
   <td>Address</td>
   <td><textarea name="address"></textarea></td>
   </tr>
   <tr>
   
   <td><input type="submit"/></td>
   </tr>
   </table>
   </center>
   </form>
   </div>
     
	<div id="footer">
	<div id="f1"><center><h3>Created By--</h3><br/>Shikha sahu<br/>Copyrite &copy</center>
	   
	
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