#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "code"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('a')
#print n
e=data.getvalue('email')
#print e
p=data.getvalue('password')
#print p
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
#print "hii"
if n=='doctor':
 query="select * from tbl_doctor where email='"+e+"'and password='"+p+"'"
 print query
 cur=con.cursor()
 a=cur.execute(query)
 con.commit()
 con.close()
 if a==1:
  print "<script>window.location.href='drprofile.py'</script>"
 else:
  print "<script>window.location.href='login.py'</script>"
if n=='patient':
 query="select * from tbl_patient where email='"+e+"'and password='"+p+"'"
 cur=con.cursor()
 a=cur.execute(query)
 con.commit()
 con.close()
 if a==1:
  print "<script>window.location.href='patientprofile.py?id="+e+"'</script>"
 else:
  print "<script>window.location.href='login.py'</script>"