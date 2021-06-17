#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "logcode wala page"
import cgi
import MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
#print n
e=data.getvalue('email')
#print e
mob=data.getvalue('mob')
#print mob
m=data.getvalue('mess')
#print m
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_contact(name,email,mobile,massage,date) values ('"+n+"','"+e+"','"+mob+"','"+m+"',curdate())"
cur=con.cursor()
cur.execute(query)
con.commit()
con.close()	
print "thanks"
