#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "ap wala page"
import cgi,MySQLdb
data=cgi.FieldStorage()
id=data.getvalue('id')
#print id
name=data.getvalue('ptname')
#print pn
appdate=data.getvalue('dt')
#print appdate
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_appointment(docid,pname,doa,date,status) values ('"+id+"','"+name+"','"+appdate+"',curdate(),'y')"
cur=con.cursor()
cur.execute(query)
con.commit()
con.close()
print "Appointment Booked"

