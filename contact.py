#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Register here"  
print """
<html>
<head>
<style>
#outer
{
height:1000;
width:100%;
background-image:url("images/4.jpg");
border:1px solid;
//background-color:red;
background-size:cover;
}
#center
{
height:900px;
width:90%;
//border:2px solid;
margin-left:5%;
margin-right:2%;
margin-top:3%;
color:white;
background-color:black;
#opacity:0.5;
#border-radius:10px;
font-size:10px;
margin-bottom:1px;
}
#header
{
height:90px;
width:100%;
border:1px solid;
#background-color:white;
#opacity:0.5;
}
#nav ul
{
list-style:none; 
margin-left:15px;
}
#nav ul li
{
float:left;
font-size:20px;
text-align:center;
border:2px solid white;
height:45px;
width:175px;
border-radius:20px;
margin-left:2px;
margin-top:10px ;	
background-color:#00002f;
}
#nav ul li a
{
text-decoration:none;
font-family:calibri;
font-size:30px;
display:block;
color:white;
}
#nav ul li a:hover
{
height:50px;
width:200px;
margin-left:-4px;
margin-top:-4px;
border-radius:10px;
border:2px solid #00293e;
color:#00293e;
text-decoration:none;
background-color:white;
}
#col1
{
height:400px;
width:100%;
//border:1px solid;
background-color:black;
opacity:0.5;
}
#left
{
height:400px;
width:50%;
background-color:black;
font-size:23px;
}
#right
{
height:400px;
width:50%;
background-color:black;
float:right;
font-size:22px;
}
#col2
{
height:300px;
width:100%;
background-color:red;
opacity:0.5;
}
#fotter
{
height:108px;
width:100%;
background-color:yellow;
opacity:0.5;
}
</style>
</style>
<body>
<div id="outer">
<div id="center">
   <div id="header">
     <div id="nav">
	 <ul>
       <li> <a href="#">Home</a></li>
       <li> <a href="#">Doctor</a></li>
       <li> <a href="#">Patient</a></li>
       <li> <a href="#">Login</a></li>
       <li> <a href="#">About</a></li>
       <li> <a href="#">Contact Us</a></li>
     </ul>
	 </div>
   </div>
<div id="col1">
   <div id="left">
   <form action="contactcode.py" method="post"><br/><br/>
     <center>NAME</center>&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
	 &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
	 <input type="text" name="name"/><br/><br/>
     <center>EMAIL</center>&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
	 &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
     <input type="email" name="email"/><br/><br/>	
    <center>MOBILE NO</center>&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
	 &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
     <input type="number" name="mob"/><br/><br/>
     <center>MESSAGE</center>&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
	 &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
     <input type="textarea" name="mess"/><br/><br/>
     <center><input type="submit" value="send"/></center>	 
   
   </form>
   
   
   </div>
   <div id="right">
    <form action="contactcode.py" method="post"><br/><br/>
     <center>ADDRESS</center><br/>&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
	 &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
    <textarea name="text" style="height:150px; width:300px;"></textarea>	
   </form>
   </div>

</div>
<div id="col2"></div>
<div id="fotter"></div>
__
<div>
</div>
</body>
</html>
"""