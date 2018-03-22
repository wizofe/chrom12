#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()

print ("Content-Type: text/html\n")

form = cgi.FieldStorage()

def user():
    name = form['name'].value
    return name
def query():
    user_query = form['query'].value
    return user_query
def search():
    search = form['gene_search'].value
    return search
