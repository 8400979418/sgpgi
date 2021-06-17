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
  <li> <a href="index.html">View Appointment<a/></li>
  <li> <a href="doctor.py">Cancel Appointment<a/></li>
  <li> <a href="patient.py">Update profile<a/></li>
  <li> <a href="login.py">Change password<a/></li>
  <li> <a href="logout.py">Logout<a/></li>
  
</ul>
</div>
</div>
</body>
</html>
"""