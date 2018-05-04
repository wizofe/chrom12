#    Database API for middler layer

import pymysql.cursors
import dbconnection


#    Get all genes information and return results as tuple
def getGene_all():
    connection = dbconnection.getConnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence FROM Gene'
    cursor = connection.cursor()
    gene_info = cursor.execute(sql)
    return gene_info
    
    connection.commit()
    connection.close()

#    Get Gene info by accession number and return results as tuple
def getGene_accno():
    connection = dbconnection.getConnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence FROM Gene WHERE Accession_No = %s '
    cursor = connection.cursor()
    geneinfo_by_accno = cursor.execute(sql)
    return geneinfo_by_accno
    
    connection.commit()
    connection.close()
    
#    Get Gene info by gene idenitifer and return results as tuple
def getGene_gi():
    connection = dbconnection.getConnection()
    sql = 'SELECT Accession_No, Gene_Identifier, Chromosomal_Location, Organism, Sequence_Length, DNA_Sequence FROM Gene WHERE Gene_Identifier = %s '
    cursor = connection.cursor()
    geneinfo_by_gi = cursor.execute(sql)
    return geneinfo_by_gi
    
    connection.commit()
    connection.close()

#    Get all Protein information and return results as tuple
def getProtein_all():
    connection = dbconnection.getConnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein'
    cursor = connection.cursor()
    pro_info = cursor.execute(sql)
    return pro_info
    
    connection.commit()
    connection.close()
    

#    Get Protein information by Accession_No and return results as tuple
def getProinfo_accno():
    connection = dbconnection.getConnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein WHERE Accession_No = %s '
    cursor = connection.cursor()
    pro_by_accno = cursor.execute(sql)
    return pro_by_accno
    
    connection.commit()
    connection.close()


#    Get Protein information by protein name and return results as tuple
def getProinfo_name():
    connection = dbconnection.getConnection()
    sql = 'SELECT Accession_No, Protein_id, Protein_name, Amino_acid_sequence from Protein WHERE Protein_name = %s '
    cursor = connection.cursor()
    pro_by_name = cursor.execute(sql)
    return pro_by_name
    
    connection.commit()
    connection.close()

#    Get all CDS info and return results as tuple
def getCDS():
    connection = dbconnection.getConnection()
    sql = 'SELECT Accession_No, Gene_Identifier,CDS_start, CDS_end, CDS_Sequence FROM Gene'
    cursor = connection.cursor()
    CDS_info = cursor.execute(sql)
    return CDS_info
    
    connection.commit()
    connection.close()

#    Get condon usage per entry by accession number and return results as tuple
def getCodonUsage():
        connection = dbconnection.getConnection()
        sql = 'SELECT Accession_No, Amacid, Codon, Number, per1000, Fraction from CondonUsage_per_entry WHERE=%s'
        cursor = connection.cursor()
        CodonUsage = cursor.execute(sql)
        return CodonUsage
        
        connection.commit()
        connection.close()


#    Get overall codon usage in chromsome 12
def getCodonUsage_chrom():
        connection = dbconnection.getConnection()
        sql = 'SELECT Amacid, Codon, Number, per1000, Fraction from CondonUsage_per_chrom12'
        cursor = connection.cursor()
        CodonUsage_chrom = cursor.execute(sql)
        return CodonUsage_chrom
        
        connection.commit()
        connection.close()

    
    
    
    
    