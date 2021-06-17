#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print "code wala page"
import cgi, MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
#print n
fn=data.getvalue('fname')
#print fn
g=data.getvalue('a')
#print g
e=data.getvalue('email')
#print e
p=data.getvalue('password')
#print p
m=data.getvalue('mobile')
#print m
s=data.getvalue('special')
#print s
f=data.getvalue('fees')
#print f
a=data.getvalue('timing')
#print a
ad=data.getvalue('address')
#print ad
sum=data.getvalue('sum')
total=data.getvalue('t')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
print sum
query="insert into tbl_doctor(doctorname,fathername,gender,email,password,mobile,speciality,fees,timing,address,date) values('"+n+"','"+fn+"','"+g+"','"+e+"','"+p+"','"+m+"','"+s+"','"+f+"','"+a+"','"+ad+"',curdate())"
cur=con.cursor()
if sum==total:
 a=cur.execute(query)
 print a
 con.commit()
 con.close()
 print "thanks"
 if a==1:
  print "<script>window.location.href='login.py'</script>"
 else:
  print "<script>alert('Invalid Captchar');window.location.href='doctor1.py';</script>"
else:
 print "<script>alert('hello bhai');</script>"