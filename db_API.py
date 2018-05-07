#!/usr/bin/env python3

"""
Program: database API
File: db_API.py

Version: V2.0
Date: 06.05.18
Function: To create database and to retrieve information from the database for middle layer
Copyright (c) 2018, Jenny Su, Birkbeck, 2018
Author: Jenny Su
See the LICENSE.txt for licensing information

Database tier of implementation of a Chromosome (12) Browser
MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
Taught by: Dr. Andrew C.R. Martin. UCL

Description:
============
This program contains functions that are used by Genbank_parser.py to create database
and functions for middle layer to retrieve relevent information from the database. 

Usage: Genbank_parser.py and middle layer

Revision History:
V1.0   02.05.18

"""
#********************************************************************************************************
#Import libraries

import pymysql
import dbconnection

#*********************************************************************************************************

def create_tables(table_names, columns_data_list):
    """this function is used by Genbank_parser.py to create tables in the database
    """

    connection = dbconnection.getdbconnection()

    for i in range(len(table_names)):
        table_name = table_names[i]
        columns_data = columns_data_list[i]

        table_create_sql = "CREATE TABLE IF NOT EXISTS %s(" % table_name
        for column_info in columns_data:
            table_create_sql += " " + column_info[0] + " " + column_info[1] + ","

        table_create_sql = table_create_sql[:-1] + ")"
        

        cursor = connection.cursor()
        cursor.execute(table_create_sql)
        connection.commit()

    connection.close()
    

def create_indexes(index_info):
    """this function is used by Genbank_parser.py to create indexes in the database
    """
    
    
    connection = dbconnection.getdbconnection()

    for table in index_info.keys():
        
        sql = "ALTER TABLE %s ADD INDEX (%s)" %(table, ', '.join(index_info[table][1]))
        

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

    connection.close()


def insert_row(table_name, columns, values):
    """this function is used by Genbank_parser.py to insert information as row to table in the database
    """
    connection = dbconnection.getdbconnection()
    try:
        sql = 'INSERT INTO %s (%s) VALUES (' % (table_name, ", ".join(columns))

        for value in values:

            if type(value) == str:
                sql += '"%s"' % value + ", "
            else:
                sql += str(value) + ", "

        sql = sql[:-2] + ")"
        

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

    except pymysql.err.IntegrityError:
        pass

    connection.close()


def fetch_one(table_name, select_columns, where_dict):
    connection = dbconnection.getdbconnection()

    sql = 'SELECT %s FROM %s WHERE ' % (", ".join(select_columns), table_name)
    for key in where_dict.keys():
        if type(where_dict.get(key)) == str:
            sql += '%s = "%s" AND ' % (key, where_dict.get(key))

        else:
            sql += '%s = %s AND ' % (key, where_dict.get(key))

    sql = sql[:-5]
    
    cursor = connection.cursor()
    cursor.execute(sql)

    row = cursor.fetchone()

    connection.close()

    return row



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
    

def getGene_acno(acno):
    
    """
    Fetches gene information from the database by their accession number
    return: row (tuple) with values of Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence
    """    
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence ' \
          'FROM Gene WHERE Accession_No = "%s"' % acno
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    
    connection.close()
    


def getGene_gi(gene_identifier):
    
    """
    Fetches gene information from the database by gene identifier
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
    return: row (tuple) with values of accession_No, Protein_id, Protein_name, Amino_acid_sequence
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
        return: row (tuple) with values of accession_No, Protein_id, Protein_name, Amino_acid_sequence
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein ' \
          'WHERE Accession_No = "%s"' % acno
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    
    connection.close()



def getProinfo_name(protein_name):
    
    """Fetches protein information from the database by protein name
       return: row (tuple) with values of accession_No, Protein_id, Protein_name, Amino_acid_sequence
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein ' \
          'WHERE Protein_name = "%s"' % protein_name
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
       args: none
       return: row (tuple) with values of Amacid, Codon, Number, per1000, Fraction for the that entry
    """
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Amacid, Codon, Number, per1000, Fraction from CodonUsage_per_Entry' \
          'WHERE Accession_No = "%s"' % acno
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

    # print (fetch_one('Codon', ['Codon_id'], {'Codon': 'TGT', 'Amacid': 'Cys'}).get('Codon_id'))


