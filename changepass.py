#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
   <head>
   </head>
   <body>
   <form action="cpcode.py" method="post">
    <table>
	  <tr>
	     <td>Enter Email Id :</td>
		 <td>
		   <input type="email" name="email" required />
		 </td>
	  </tr>
	  <tr>
	    <td>Enter Old Password :</td>
	    <td>
	  <input type="password" name="oldpass" required />	
		</td>
	  </tr>
	  <tr>
	    <td>Enter New Password :</td>
	    <td>
	<input type="password" name="newpass" required />
		</td>
	  </tr>
	  <tr>
	    <td>Enter Confirm Password :</td>
	    <td>
		<input type="password" name="cpass" required />
		</td>
	  </tr>
	  <tr>
	     <td colspan="2" align="center">
		 <input type="submit" value="Change Password" />
		 </td>
	  </tr>
	</table>
	</form>
   </body>
</html>
"""