#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
print ("Content-Type: text/html\n")

form = cgi.FieldStorage()
query_type = form['query_type'].value
query = form['query'].value
gene_dict = {'g1':'gene1','g2':'gene2','g3':'gene3','g4':'gene4'}
prot_dict = {'p1':'prot1','p2':'prot2','p3':'prot3','p4':'prot4'}
re_dict = {'r1':'re1','r2':'re2','r3':'re3','r4':'re4'}

if query_type == 'gene':
    dict = gene_dict
elif query_type == 'protein':
    dict = prot_dict
else:
    dict = re_dict

def result():
    if query in dict:
        result = dict[query]
    else:
        result = 'Oops!! Result not found,refine your search and try again'
    return result

html = '<html>'
html += '<head>'
html += '<title> Result page </title>'
html += "<style>"
html += "body{background-color: #323232;color:white;}"
html += "</style>"
html += '</head>'
html += '<body>'
html += '<h4><b>Result as below</b></h4>'
html += '<p>'+ result() + '</p>'
html += '</body>'
html += '</html>'
print(html)
