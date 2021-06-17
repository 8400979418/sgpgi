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
<h1>Patient</h1>
<form action="patientcode.py" method="post" style="margin-top:10px;">
Name&nbsp&nbsp&nbsp&nbsp<input type="text" name="name"  style="border-radius:10px;"/><br/><br/>
Father &nbsp&nbsp&nbsp&nbsp<input type="text" name="fname"  style="border-radius:10px;"/><br/><br/>
Gender&nbsp&nbsp&nbsp&nbsp<input type="radio" name="a" value="male"/>male
&nbsp&nbsp&nbsp&nbsp<input type="radio" name="a" value="female" />female<br/><br/>
Email &nbsp&nbsp&nbsp&nbsp<input type="email" name="email" style="border-radius:10px;"  /><br/><br/>
Password &nbsp&nbsp&nbsp&nbsp<input type="password" name="password" style="border-radius:10px;" /><br/><br/>
Mobile&nbsp&nbsp&nbsp&nbsp<input type="number" name="mobile" style="border-radius:10px;"/><br/><br/>
Address&nbsp&nbsp&nbsp&nbsp<input type="textarea" name="address" style="border-radius:10px;"/><br/><br/>
<input type="submit"/><br/><br/>
</form>
</div>
</div>
</center>
</body>
</html>
"""  