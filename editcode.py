#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
name=data.getvalue('name')
fname=data.getvalue('fname')
gender=data.getvalue('gender')
mobile no.=data.getvalue('mob')
email=data.getvalue('email')
address=data.getvalue('add')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
query="update tbl_patient set name='"+name+"',fname='"+fname+"',gender='"+gender+"',mobileno='"+mob+"',address='"+add+"' where email='"+email+"'"
cur.execute(query)
print "<script>window.location.href ='patiprofile.py?id="+email+"';</script>"