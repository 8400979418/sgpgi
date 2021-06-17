#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "code wala page"
import cgi,MySQLdb
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
ad=data.getvalue('address')
#print ad
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_patient(name,fname,gender,email,password,mobile,address,date) values('"+n+"','"+fn+"','"+g+"','"+e+"','"+p+"','"+m+"','"+ad+"',curdate())"
cur=con.cursor()
cur.execute(query)
con.commit()
con.close()
print "thanks"
