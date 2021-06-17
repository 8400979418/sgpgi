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
e=data.getvalue('email')
#print e
p=data.getvalue('password')
#print p
a=data.getvalue('address')
#print a
s=data.getvalue('specci')
#print s
t=data.getvalue('timing')
#print t
exp=data.getvalue('exp')
#print exp
fee=data.getvalue('fee')
#print fee
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_doctor(name,fname,email,password,address,specification,timing,fee,expricence,date) values ('"+n+"','"+fn+"','"+e+"','"+p+"','"+a+"','"+s+"','"+t+"','"+fee+"','"+exp+"',curdate())"
cur=con.cursor()
cur.execute(query)

con.commit()
con.close()	
print "thanks"

