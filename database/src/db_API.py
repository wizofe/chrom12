#!/usr/bin/env python3

"""
Program: database API
File: db_API.py

Version: V2.0
Date: 06.05.18
Function: To retrieve information from the database to middle layer
Copyright (c) 2018, Jenny Su, Birkbeck, 2018
Author: Jenny Su
See the LICENSE.txt for licensing information

Database tier of implementation of a Chromosome (12) Browser
MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
Taught by: Dr. Andrew C.R. Martin. UCL

Description:
============
This program contains functions for middle layer to retrieve relevent information from the database

Usage: For middle layer

Revision History:
V1.0   02.05.18

"""
#********************************************************************************************************
#Import libraries

import pymysql
import dbconnection

#*********************************************************************************************************

def getGene_all():
    
    """Fetches gene information from the database
       args:none
       return: row (tuple) with values of Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence
    """
    
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence FROM Gene'
    cursor = connection.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        yield row

    connection.close()

def getGene_proteinid():
    
    """Fetches gene information from Gene table and protein id from protein table in the database
       args:none
       return: row (tuple of strings) with values of Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length,
       DNA_Sequence, Protein_id
    """
    
    connection = dbconnection.getdbconnection()
    sql = 'SELECT g.Accession_No, g.Gene_Identifier, g.Chromosomal_Location, g.Organism, g.Sequence_Length, g.DNA_Sequence, p.Protein_id '\
          'FROM Gene g, Protein p '\
          'WHERE g.Accession_No = p.Accession_No'
    cursor = connection.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        yield row

    connection.close() 
    

def getGene_acno(acno):
    
    """
    Fetches gene information from the database by their accession number
    args: acno (from user input)
    return: row (tuple) with values of Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence
    """    
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence FROM Gene WHERE Accession_No = "%s" ' %(acno)
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    
    connection.close()
    


def getGene_gi(gene_identifier):
    
    """
    Fetches gene information from the database by gene identifier
    args: gene_identifier (from user input)
    return: row (tuple) with values of Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence ' \
          'FROM Gene WHERE Gene_Identifier = "%s" ' % gene_identifier
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row
    
    
    connection.close()



def getProtein_all():
    
    """Fetches protein information from the database
    args: none
    return: row (tuple of strings ) with values of accession_No, Protein_id, Protein_name, Amino_acid_sequence
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein'
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    
    connection.close()
    

def getProinfo_acno(acno):
    
    """Fetches protein information from the database by Accession_No
       args: acno (from user input)
       return: row (tuple) with values of accession_No, Protein_id, Protein_name, Amino_acid_sequence
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein WHERE Accession_No = "%s"' % acno
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    
    connection.close()



def getProinfo_name(protein_name):
    
    """Fetches protein information from the database by protein name
       args: protein_name (from user input)
       return: row (tuple) with values of accession_No, Protein_id, Protein_name, Amino_acid_sequence
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein WHERE Protein_name LIKE "%s%%" ' % protein_name
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    
    connection.close()



def getCDS():
    
    """Fetches CDS information from the database
       args: none
       return: row (tuple) with values of Accession_No, Gene_Identifier,CDS_start, CDS_end, CDS_Sequence
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier,CDS_start, CDS_end, CDS_Sequence FROM Gene'
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    
    connection.close()



def getCodonUsage(acno):
    
    """Fetches condon usage per entry by accession number from the database
       args: acno (accession number from user input)
       return: row (tuple) with values of Amacid, Codon, Number, per1000, Fraction for the that entry
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Amacid, Codon, Number, per1000, Fraction From CodonUsage_per_Entry WHERE Accession_No = "%s" ' %(acno)
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    
    connection.close()



def getCodonUsage_chrom():
    """Fetches condon usage information of chromosome 12 from database 
       args: none
       return: row (tuple) with values of Amacid, Codon, Number, per1000, Fraction
    """
    
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Amacid, Codon, Number, per1000, Fraction from CodonUsage_per_chrom'
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row


    connection.close()


if __name__ == "__main__":
    for row in getCodonUsage_chrom():
        print(row)



