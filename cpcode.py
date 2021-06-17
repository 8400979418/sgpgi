#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
email=f.getvalue('email')
oldpass=f.getvalue('oldpass')
newpass=f.getvalue('newpass')
cpass=f.getvalue('cpass')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()

st="false"
query="select password from tbl_patient where email='"+email+"'"

cur.execute(query)
res=cur.fetchall()
p=""
for r in res:
 p=r[0]
 st="true"

if newpass==cpass and oldpass==p and st=="true":
 q="update tbl_patient set password='"+newpass+"' where email='"+email+"'"
 n=cur.execute(q)
 if n==1:
  print "<script>alert('New Password Updated');window.location.href='changepass.py';</script>"
 else:
  print "<script>alert('not updated');window.location.href='changepass.py';</script>"
else:
 print "<script>alert('new password or old password is not matched');window.location.href='changepass.py';</script>"
  