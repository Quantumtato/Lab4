#!/usr/bin/python37all
import cgi
import json
data = cgi.FieldStorage()
s1 = data.getvalue('slider1')
s2 = data.getvalue('option')
imput = {"slider1":s1, "option":s2}

with open('lab4.txt', 'w') as f:  
  json.dump(imput,f)

print('Content-type: text/html\n\n')

print(""" 
<html>
<form action="/cgi-bin/lab4.py" method="POST">
 	<input type="radio" name="option" value="1" checked> Red LED <br>
 	<input type="radio" name="option" value="2"> Green LED <br>
 	<input type="radio" name="option" value="3"> Blue LED <br>
  <input type="submit" value="Submit">
</form>
<form action="/cgi-bin/lab4.py" method="POST">
<input type="range" name="slider1" min ="0" max="100" value ="0"><br>
<input type="submit" value="Change LED brightness">
</form>
</html>
""")