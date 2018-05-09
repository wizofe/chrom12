#!/usr/bin/env python
import cgi
import cgitb
import json

cgitb.enable()
#print("Content-Type:text/html\n")
def gene_summ():
    summary = getGene_all()
    return summary



result = '{"gene_id":["g1","g2","g3","g4"],"acc_num":["a1","a2","a3","a4"],"protein":["p1","p2","p3","p4"],"chromo_location":["q1","q2","q3","q4"]}'
r=json.loads(result)
def vari():
    return result

#print(r)
#print (type(r))
def html():
    html = "<html lang='en'>"
    html += "<head>"
    html += "<title>Midlle Layer</title>"
    html += "<style>"
    html += '<link rel ="stylesheet" type="text/css" href="http://localhost/chrom12/frontlayer/src/html/main.css">'
    html += "</style>"
    html += "</head>"
    html += "<style>"
    html += '''body{
    color:#660099;
    text-align: center;
    background-size:cover;
    background-color: rgba(255,255,255,0.7);
    background-blend-mode: lighten;
    background-image: url('http://localhost/chrom12/frontlayer/src/img/chromo1.jpg');
    background-repeat: no-repeat;
    margin-bottom:50px;
    }'''
    html += '</style>'
    html += "<body>"
    html += '<p style=font-weight:bold>'+r['gene_id']+'</p>'
    html += '</body>'
    html += '</html>'
    print(html)
if __name__== "__main__":
    html()
