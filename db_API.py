# Copyright (c) 2018, Jenny Su
# See the LICENSE.txt for licensing information
#
# Database tier of implementation of a Chromosome (12) Browser
# MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
# Taught by: Dr. Andrew C.R. Martin. UCL
#    Database API for middler layer

import pymysql
import dbconnection


def create_tables(table_names, columns_data_list):

    connection = dbconnection.getdbconnection()

    for i in range(len(table_names)):
        table_name = table_names[i]
        columns_data = columns_data_list[i]

        table_create_sql = "CREATE TABLE IF NOT EXISTS %s(" % table_name
        for column_info in columns_data:
            table_create_sql += " " + column_info[0] + " " + column_info[1] + ","

        table_create_sql = table_create_sql[:-1] + ")"
        # print(table_create_sql)

        cursor = connection.cursor()
        cursor.execute(table_create_sql)
        connection.commit()

    connection.close()


def create_indexes(index_info):

    connection = dbconnection.getdbconnection()

    for table in index_info.keys():
        # sql = "CREATE INDEX %s ON %s (%s)" %(index_info[table][0], table, ', '.join(index_info[table][1]))
        sql = "ALTER TABLE %s ADD INDEX (%s)" %(table, ', '.join(index_info[table][1]))
        # print(sql)

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

    connection.close()


def insert_row(table_name, columns, values):
    connection = dbconnection.getdbconnection()
    try:
        sql = 'INSERT INTO %s (%s) VALUES (' % (table_name, ", ".join(columns))

        for value in values:

            if type(value) == str:
                sql += '"%s"' % value + ", "
            else:
                sql += str(value) + ", "

        sql = sql[:-2] + ")"
        # print(sql)

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
        # elif type(where_dict.get(key)) == int:
        #     sql += '%s = "%s" AND ' % (key, where_dict.get(key))
        else:
            sql += '%s = %s AND ' % (key, where_dict.get(key))

    sql = sql[:-5]
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)

    row = cursor.fetchone()

    connection.close()

    return row


#    Get all genes information and return results as tuple
def getGene_all():
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence FROM Gene'
    cursor = connection.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        yield row

    connection.close()
    # connection.commit()



#    Get Gene info by accession number and return results as tuple
def getGene_acno(acno):
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence ' \
          'FROM Gene WHERE Accession_No = "%s"' % acno
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    # connection.commit()
    connection.close()
    

#    Get Gene info by gene idenitifer and return results as tuple
def getGene_gi(gene_identifier):
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence ' \
          'FROM Gene WHERE Gene_Identifier = "%s" ' % gene_identifier
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row
    
    # connection.commit()
    connection.close()


#    Get all Protein information and return results as tuple
def getProtein_all():
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein'
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    # connection.commit()
    connection.close()
    

#    Get Protein information by Accession_No and return results as tuple
def getProinfo_acno(acno):
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein ' \
          'WHERE Accession_No = "%s"' % acno
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    # connection.commit()
    connection.close()


#    Get Protein information by protein name and return results as tuple
def getProinfo_name(protein_name):
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein ' \
          'WHERE Protein_name = "%s"' % protein_name
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    # connection.commit()
    connection.close()


#    Get all CDS info and return results as tuple
def getCDS():
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Gene_Identifier,CDS_start, CDS_end, CDS_Sequence FROM Gene'
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    # connection.commit()
    connection.close()


#    Get condon usage per entry by accession number and return results as tuple
def getCodonUsage():
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Accession_No, Amacid, Codon, Number, per1000, Fraction from CodonUsage_per_Entry'
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    # connection.commit()
    connection.close()


#    Get overall codon usage in chromsome 12
def getCodonUsage_chrom():
    connection = dbconnection.getdbconnection()
    sql = 'SELECT Amacid, Codon, Number, per1000, Fraction from CodonUsage_per_chrom'
    cursor = connection.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        yield row

    # connection.commit()
    connection.close()


if __name__ == "__main__":
    for row in getCodonUsage_chrom():
        print(row)

    # print (fetch_one('Codon', ['Codon_id'], {'Codon': 'TGT', 'Amacid': 'Cys'}).get('Codon_id'))


