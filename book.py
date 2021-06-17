#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Register here"
  
print """
<form action="bookcode.py" method="post">
specialization
<select name="spec">
 <option value="">CHOOSE SPECIALITY</option>
"""
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="select distinct specification from tbl_doctor"
cur=con.cursor()
cur.execute(query)
res=cur.fetchall()
for r in res:
 print '<option>'+r[0]+'</option>'
print"""
</select>
<input type="submit" value="search doctor"/>
</form>
"""                                                                                                         

