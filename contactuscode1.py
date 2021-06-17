#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "code wala page"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
#print n
e=data.getvalue('email')
#print e
m=data.getvalue('mobileno')
#print m
me=data.getvalue('message')
#print me
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_contact(name,email,mobileno,message) values ('"+n+"','"+e+"','"+m+"','"+me+"')"
#print query
cur=con.cursor()
a=cur.execute(query)
con.commit()
con.close()
print "thanks"
