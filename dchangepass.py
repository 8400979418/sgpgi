#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
  <head>
  <link href="css/changepass.css" rel="stylesheet" type="text/css"/>
  </head>
  <body>
  <div id="outer">
<div id="header">
   <div id="logo">
    <img src="images/logo.jpg" height="150px" width="150px" />
   </div>
   <div id="heading">
   
<p align="center" style="font-size:50px;"><b>Swejal Hospital</b></p>
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
   <div id="left">
   <marquee  onmouseover="stop()" onmouseout="start()">
	<img id="p" src="images/th1.jpg" height="300px" width="300px"/>
	<img id="p" src="images/th2.jpg" height="300px" width="300px" />
	<img id="p" src="images/th3.jpg" height="300px" width="300px" />
	<img id="p" src="images/th1.jpg" height="300px" width="300px" />
	<img id="p" src="images/a.jpg" height="300px" width="300px" />
	<img id="p" src="images/r.jpg" height="300px" width="300px" />
	<img id="p" src="images/th1.jpg" height="300px" width="300px" />
	<img id="p" src="images/th2.jpg" height="300px" width="300px" />
	<img id="p" src="images/th3.jpg" height="300px" width="300px" /></marquee>
   </div>
   <div id="center">
  <form action="dcpcode.py" method="post"><center>
  <h1><font color="white">Change-Password:</font></h1>
  <table>
  <tr>
  <td>Enter Email Id</td>
  <td>
  <input type="email" name="email"/>
  </td>
  </tr>
  <tr>
  <td>Enter Old Password</td>
  <td>
  <input type="password" name="oldpass"/>
  </td>
  </tr>
  <tr>
  <td>Enter New Password</td>
  <td>
  <input type="password" name="newpass"/>
  </td>
  </tr>
  <tr>
  <td>Enter Confirm Password</td>
  <td>
  <input type="password" name="cpass" required />
  </td>
  </tr>
  <tr>
  <td colspan="2" align="center">
  <input type="submit" value="Change Password" />
  </td>
  </tr>
  </table>
  </center>
  </form>
  </div>
<div id="right">

<marquee direction=right onmouseover="stop()" onmouseout="start()"><center><a href="#"><font id="co">Finance Department</font><a> <br/>
	<a href="#"><font id="co">Circular</font></a><br/>
	<a href="#"><font id="co">Patient Portal Direct Online Registration</font></a><br/>
	<a href="#"><font id="co">Swejal Hospital Act 1983</font></a><br/>
	<a href="#"><font id="co">Swejal Hospital Regulation</font></a><br/>
	<a href="#"><font id="co">Centeral Library</font></a><br/>
	<a href="#"><font id="co">Finance Dept</font></a><br/>
	<a href="#"><font id="co">Swejal Hospital Alumni</font></a><br/>
	<a href="#"><font id="co">Download form/Office Orders</font></a><br/>
	<a href="#"><font id="co">Swejal Hospital Newslatter</font></a><br/>
	<a href="#"><font id="co">RTI Act</font></a><br/>
	</center>
	</marquee>
</div>
	</div>
	<br/>
	<div id="footer">
	<div id="f1"><center><h3>Created By--</h3><br/>Shikha sahu <br/>Copyrite &copy</center>
	   
	
	</div>
	
	
	<div id="f2"><center><h3>About Us--</h3></center><br/><p>Swejal Hospital
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