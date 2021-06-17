#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="select * from  tbl_appointment"
cur.execute(q)
res=cur.fetchall()
print """
<table style="margin:0px auto;width:60%;" border="1">
<tr>
<th>APP.ID</th>
<th>Doc ID</th>
<th>PATIENT NAME</th>
<th>DOA</th>
<th>POST DATE</th>
<th>STATUS</th>
</tr>
"""
for r in res:
 print "<tr>"
 print "<td>",r[0],"</td>"
 print "<td>",r[1],"</td>"
 print "<td>",r[2],"</td>"
 print "<td>",r[3],"</td>"
 print "<td>",r[4],"</td>"
 print "<td>",r[5],"</td>"
 print "</tr>"

print """
</table>
"""




