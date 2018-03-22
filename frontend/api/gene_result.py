#!/usr/bin/env python
from gene import query
user_query = query()

def get_result():
    gene_dict = {'g1':'gene1','g2':'gene2','g3':'gene3','g4':'gene4'}
    if user_query in gene_dict:
        result = gene_dict[user_query]
    else:
        result = 'Oops!! Result not found,refine your search and try again'
    return result
