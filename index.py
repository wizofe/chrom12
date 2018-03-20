#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
print ("Content-Type: text/html\n")

form = cgi.FieldStorage()
name = form['name'].value
query_type = form['query'].value

html = '<html>'
html += '<head>'
html += '<title> Welcome  ' + name + '</title>'
html += '</head>'
html += '<body>'
html += "<p>Thanks for visiting our page  "'<b>' +name+ '</b>'"<p></br>"
if query_type == 'gene':
    html += "<a href='http://localhost/project/gene.html'>gene Information</a>"
elif query_type == 'protein':
    html += "<a href='http://localhost/project/protein.html'>Protein Information</a>"
else:
    html += "<a href='http://localhost/project/re.html'>RE</a>"

html += '</body>'
html += '</html>'
print(html)


'''choice = cgi.getlist('dropdown')
for choice in dropdown:
    if choice == 'gene':'''
