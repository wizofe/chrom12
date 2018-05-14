#!/usr/bin/env python3

"""*************************************************************************************************
* project: Genome browse for chromosome-12                                                         *
* file:gene_summary.py                                                                             *
* Date: 08/05/2018                                                                                 *
* version:v1.0 ,v2.0(updated on 13/05/18                                                           *
* Function : This python script generate result page according to user input in search          *                                         *
* Licence:See the LICENSE.txt for licensing information                                            *
* Author: Abdulvahab Kharadi                                                                       *
* ***********************************************************************************************"""

# Import required Modules
import cgi
import cgitb
from front_api import gene_summ
cgitb.enable()
print("Content-Type:text/html\n")

summary=gene_summ()

# This html function creates Summary page for Genes in Chromosome-12.
def html():
    html ='<html lang="en">'
    html += '<head>'
    html += "<title>Chromosome-12 Information</title>"
    html += "<meta charset='utf-8'>"
    html += "<meta name='viewport' content='width=device-width,initial-scale=1.0'>"
    html += '<link rel ="stylesheet" type="text/css" href = "http://localhost/chrom12/frontlayer/src/html/main.css">'
    #html += '<link rel="stylesheet" href="https://localhost/chrom12/frontlayer/src/html/main.css">'
    html += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'
    html += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'
    html += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>'
    html += "<style>"
    html += '''body{
    color:#660099;
    text-align: center;
    background-size:cover;
    background-attachment: fixed;
    background-color: rgba(255,255,255,0.7);
    background-blend-mode: lighten;
    background-image: url('chromo1.jpg');
    background-repeat: no-repeat;
    margin-bottom:50px;
    }'''
    html += "</style>"
    html += '</head>'
    
    html+='<body>'    
    html += "<div class='main-container'>"
    html += "<header ><h1>Summary of Chromosome 12</h1></header>"
    html += '<nav>'
    html += "<a href='http://student.cryst.bbk.ac.uk/~ka001/index.html'>Home  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/~ka001/gene_search.html'>Gene Search  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/~ka001/prot_search.html'>Protein Search  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/ka001/gene_summary.py'>Gene Summary  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/ka001/prot_summary.py'>Protein Summary  |</a>"
    html += "<a href='http://student.cryst.bbk.ac.uk/~ka001/contactus.html'>Contact us</a>"
    html += '</nav>'
    html += "<div class='footer'>&copy; 2018,Group Chromosome-12.</div>"
    
    html += "<table class='table table-condensed'>"
    html += "<thead style='background-color:#DEEDD3'>"
    html += "<tr>"
    html += "<th>Genebank Accssion</th>"
    html += "<th>Gene Identifires</th>"
    html += '<th>Chromosomal Location</th>'
    html += '<th>Organism</th>'
    html += '<th>DNA Sequence Length</th>'
    html += '<th>CDS Start</th>'
    html += '<th>CDS End</th>'
    html += '<th>Protein ID</th>'
    html += '<th>Expand</th>'
    html += '</tr>'
    html += '</thead>'
    
    html += '<tbody>'
    for row in summary:       
        html += '<tr>'
        html += "<td id='acc_num'>{}</td>".format(row[0])
        html += "<td id='gene_id'>{}</td>".format(row[1])
        html += "<td id='organism'>{}</td>".format(row[2])
        html += "<td id='chromo_location'>{}</td>".format(row[3])
        html += "<td id='Sequence_Length'>{}</td>".format(row[4])
        html += "<td id='CDS_start'>{}</td>".format(row[5])
        html += "<td id='CDS_end'>{}</td>".format(row[6])
        html += "<td id='Prot_id'>{}</td>".format(row[8])
        html += "<td id='Expand'><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/ka001/gene_result.py?query={}&choice=gene_acc'>Expand</a></td>".format(row[0])
        html += '</tr>'       
    html += '</tbody>'
    html += '</table>'
    
    html += '</div>'
    html += '</body>'
    html += '</html>'
    print(html)
if __name__=="__main__":
    html()
