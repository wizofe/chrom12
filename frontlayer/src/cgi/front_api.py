#!/usr/bin/env python3
"""*************************************************************************************************
* project: Genome browse for chromosome-12,Msc Bioinformatics & System Biology
* Module: Biocomuting-2 Taught By(Dr Andrew C. Martin)                                                         *
* file:front_api.py                                                                                   *
* Date: 08/05/2018                                                                                 *
* version:v1.0                                                                                     *
* Function : This python script generate result page according to user input in search             *                                         *
* Licence:See the LICENSE.txt for licensing information                                            *
* Author: Abdulvahab Kharadi                                                                       *
* ***********************************************************************************************"""

# Import requred modules to get info from database
import cgi
import cgitb
import json
from db_API import *
cgitb.enable()


def gene_summ():
    summary_gene = getGene_all()
    summary=[]
    for row in summary_gene:
        Accession_No = row['Accession_No']
        Gene_Identifier= row['Gene_Identifier']
        Organism = row['Organism']
        Chromosomal_Location = row['Chromosomal_Location']
        Sequence_Length = row['Sequence_Length']
        CDS_start = row['CDS_start']
        CDS_end = row['CDS_end']
        CDS_sequence = row['CDS_sequence']
        Protein_id = row['Protein_id']
        result = [Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, CDS_start,CDS_end,CDS_sequence,Protein_id]
        summary.append(result)
        
    #print(row)
    return summary

def gene_query_acno(q):
    res = getGene_acno(q)   
    for row in res:
        Accession_No = row['Accession_No']
        Gene_Identifier= row['Gene_Identifier']
        Organism = row['Organism']
        Chromosomal_Location = row['Chromosomal_Location']
        Sequence_Length = row['Sequence_Length']
        DNA_Sequence = row['DNA_Sequence']
        CDS_start = row['CDS_start']
        CDS_end = row['CDS_end']
        CDS_sequence = row['CDS_sequence']
        
        gene_info =[Accession_No,Gene_Identifier,Organism,Chromosomal_Location,Sequence_Length,DNA_Sequence,CDS_start,CDS_end,CDS_sequence]
        return gene_info
     #print (gene_info)

def gene_query_gi(q):
    res = getGene_gi(q)
    for row in res:
        acc_num = row['Accession_No']
        gene_id = row['Gene_Identifier']
        organism = row['Organism']
        chromo_location =row['Chromosomal_Location']
        Sequence_Length = row['Sequence_Length']
        DNA_Sequence = row['DNA_Sequence']
        CDS_start = row['CDS_start']
        CDS_end = row['CDS_end']
        CDS_sequence = row['CDS_sequence'] 
           
        gene_info = [gene_id,acc_num,organism,chromo_location,Sequence_Length,DNA_Sequence,CDS_start,CDS_end,CDS_sequence]
        return (gene_info)
    #print (result_gene)

def protein_summ():
    res = getProtein_all()
    summary=[]
    for row in res:
        acc_num = row['Accession_No']
        Protein_id = row['Protein_id']
        Protein_name = row['Protein_name']
        aa_seq = row['Amino_acid_sequence']
        result = [acc_num,Protein_id,Protein_name,aa_seq]
        summary.append(result)
    #print(summary[1])
    return summary

def protein_query_name(q):
    res = getProinfo_name(q)
    for row in res:
    	acc_num = row['Accession_No']
    	prot_id = row['Protein_id']
    	prot_name = row['Protein_name']
    	aa_seq =row['Amino_acid_sequence']
    	prot_info=[acc_num,prot_id,prot_name,aa_seq]
    	return prot_info

def protein_query_acno(q):
    res = getProinfo_acno(q)
    for row in res:
    	acc_num = row['Accession_No']
    	prot_id = row['Protein_id']
    	prot_name = row['Protein_name']
    	aa_seq =row['Amino_acid_sequence']
    	prot_info=[acc_num,prot_id,prot_name,aa_seq]
    	return prot_info
    



if __name__== "__main__":
    #html()
    #gene_summ()
    #protein_summ()
    #gene_query_acno('g1')
    #gene_query_gi('UbC')
    print('')
