#!/usr/bin/env python

from gene_result import get_result
from gene import user
html = '<html>'
html += '<head>'
html += '<title> Welcome  ' + user() + '</title>'
html += '</head>'
html += '<body>'
html += "<p>Thanks for visiting our page  "'<b>' + user() + '</b>'"<p></br>"
html += "<p>" + get_result() + "</p>"
html += '</body>'
html += '</html>'
print(html)
