#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "ersktldkrhj"
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
#form
{
height:500px;
width:350px;
margin-top:200px;
border:1px solid;
background-color:white;
border-radius:50px;
}
</style>
</head>
<body>
<center>

<div id="outer">
<div id="form"> 
<h1>LOGIN</h1>
<form action="logcode.py" method="post" style="margin-top:10px;">
Who are you<select style="border-radius:10px;" name="a">
<option value="doctor">Doctor</option>
<option value="patient">Patient</option>
</select><br/><br/>

Email &nbsp&nbsp&nbsp&nbsp<input type="email" name="email" style="border-radius:10px;"  /><br/><br/>
Password &nbsp&nbsp&nbsp&nbsp<input type="password" name="password" style="border-radius:10px;" /><br/><br/>

<input type="submit"/><br/><br/>
</form>
</div>
</div>
</center>
</body>
</html>
"""  