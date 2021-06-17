#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Register here"
import cgi,MySQLdb
data=cgi.FieldStorage()
spec=data.getvalue('spec')
#print n
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="select * from tbl_doctor where specification='"+spec+"'"
cur=con.cursor()
cur.execute(query)
res=cur.fetchall()
#now make the table
print"""
<table border='1'>
<tr>
<th>doctor name</th>
<th>specialization</th>
<th>timing</th>
<th>fees</th>
<th>book now</th>
</tr>
"""
for r in res:
 print "<tr>"
 print "<td>",r[1],"</td>"
 print "<td>",r[6],"</td>"
 print "<td>",r[8],"</td>"
 print "<td>",r[10],"</td>"
 print "<td><a href='appoint.py'>book</a></td>"
 print "</tr>"
print """
</table>"""