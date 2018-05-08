#!/usr/bin/env python
"""*************************************************************************************************
* project: Genome browse for chromosome-12,Msc Bioinformatics & System Biology
* Module: Biocomuting-2 Taught By(Dr Andrew C. Martin)                                                         *
* file:result.py                                                                                   *
* Date: 08/05/2018                                                                                 *
* version:v1.0                                                                                     *
* Function : This python script generate result page according to user input in search             *                                         *
* Licence:See the LICENSE.txt for licensing information                                            *
* Author: Abdulvahab Kharadi                                                                       *
* ***********************************************************************************************"""
import cgi
import cgitb
cgitb.enable()
print ("Content-Type: text/html\n")

form = cgi.FieldStorage()
#query_type = form['query_type'].value
query = form['query'].value
gene_dict = {'g1':'gene1','g2':'gene2','g3':'gene3','g4':'gene4'}
prot_dict = {'p1':'prot1','p2':'prot2','p3':'prot3','p4':'prot4'}
re_dict = {'r1':'re1','r2':'re2','r3':'re3','r4':'re4'}
dic_list =[gene_dict,prot_dict,re_dict]

def result():
    for dic in dic_list:
        if query in dic:
            result = dic[query]
            break
        else:
            result = 'Oops!! Result not found,refine your search and try again'
    return result
html = "<html lang='en'>"
html += '<head>'
html += '<title> Result page </title>'
#html += '<link rel ="stylesheet" type="text/css" href = "/Library/WebServer/Documents/chrom12/frontend/src/html/main.css">'
html += "<style>"
html += '''body{
color:#660099;
text-align: center;
background-size:cover;
background-color: rgba(255,255,255,0.7);
background-blend-mode: lighten;
background-image: url(/Library/Webserver/Documents/chrom12/frontend/src/img/chromo1.jpg);
background-repeat: no-repeat;
margin-bottom:50px;
}'''
html += "</style>"
html += '</head>'
html += '<body>'
html += '<h4><b>Result as below</b></h4>'
html += '<p>'+ result() + '</p>'
html += '</body>'
html += '</html>'
print(html)
def summary_result():
