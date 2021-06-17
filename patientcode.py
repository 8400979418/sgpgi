#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "logcode wala page"
import cgi
import MySQLdb
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
a=data.getvalue('address')
#print a
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_patient(name,fname,gender,email,password,mobile,address,date) values ('"+n+"','"+fn+"','"+g+"','"+e+"','"+p+"','"+m+"','"+a+"',curdate())"
cur=con.cursor()
cur.execute(query)

con.commit()
con.close()	
print "thanks"

