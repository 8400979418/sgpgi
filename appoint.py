#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
data=cgi.FieldStorage()
id=data.getvalue('did')
#print id
print """
<html>
<head>
</head>
<body>
<div id="outer">
<div id="content">
<center>
<h1 style="text-align:center;font-family:gabriola;">Enter Patient's Name and Date</h1>
<hr/>
<form action="ap.py" method="post">
Patient Name: <input type="text" name="ptname"/>
<br/><br/>
Appointment date: <input type="date" name="dt"/>
<br/><br/>
"""
print '<input type="hidden" name="id" value="id"/>'
print """
<br/><input type="submit" value="Book Appointment" style="color:white;height:40px;background-color:#024753;"/>
</form>
</center>
</div>
</div>
</body>
</html>
"""





