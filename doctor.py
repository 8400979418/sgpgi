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
<h1>Doctor</h1>
<form action="doccode.py" method="post" style="margin-top:10px;">
Name<input type="text" name="name"  style="border-radius:10px;"/><br/><br/>
Father name<input type="text" name="fname"  style="border-radius:10px;"/><br/><br/>
Email<input type="email" name="email"=style="border-radius:10px;"  /><br/><br/>
Password<input type="password" name="password" style="border-radius:10px;" /><br/><br/>
Address<input type="textarea" name="address"  style="border-radius:10px;"/><br/><br/>
Specification<select name="specci"style="border-radius:10px;">
<option>Specification</option>
<option>Surgon</option>
<option>Physician</option>
<option>Eye specialist</option>
<option>Orthopedician</option>
<option>Dentist</option>
<option>Cardilogist</option>
</select><br/><br/>
Timing<select name="timing" style="border-radius:10px;">
<option>Timing</option>
<option>7:00pm-10:00pm</option>
<option>10:00pm-1:00am</option>
<option>1:00am-4:00pm</option>
<option>4:00pm-8:00pm</option>
</select><br/><br/>
Expricence<input type="text" name="exp" style="border-radius:10px;"/><br/><br/>
Fee<input type="text" name="fee" style="border-radius:10px;"/><br/><br/>

"""
import random
a=[0,1,2,3,4,5,6,7,8,9]
n1=random.choise(a)
n2=random.choise(a)
sum=n1+n2
print "<td>"
print "<input value='"+str(n1)+"' 'style=width:20px;' readonly />"
print "<input value='"+str(n2)+"' 'style=width:20px;' readonly />"
print " = " <input type='number' name='t' style='width=50px' required />"
print "</td>"
print"""

<input type="submit"/>
</form>
</div>
</div>
</center>
</body>
</html>
"""  