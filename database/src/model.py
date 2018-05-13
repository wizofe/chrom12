#!/usr/bin/env python3

"""
Program: model
File: model.py

Version: V2.0
Date: 06.05.18
Copyright (c) 2018, Jenny Su, Birkbeck, 2018
Author: Jenny Su
See the LICENSE.txt for licensing information

Database tier for implementation of a Chromosome (12) Browser
MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
Taught by: Dr. Andrew C.R. Martin. UCL

Description:
============
This program contains models for database tables construction and is used by Genbank_parser.py to create the chromosome database.
Each model maps to a single database table and contains fields and behaviors of the data being stored.  

Usage: Genbank_parser.py

Revision History
V1.0 04.05.18

"""
#****************************************************************

gene_columns = [
    ("Accession_No", "VARCHAR(20) PRIMARY KEY"),
    ("Gene_Identifier", "VARCHAR(200)"),
    ("Chromosomal_location", "VARCHAR(200)"),
    ("Organism", "VARCHAR(20)"),
    ("Sequence_Length", "INT"),
    ("DNA_Sequence", "LONGTEXT"),
    ("CDS_start", "INT"),
    ("CDS_end", "INT"),
    ("CDS_sequence", "TEXT")
]

protein_columns = [
    ("Accession_No", "VARCHAR(20)"),
    ("Protein_id", "VARCHAR(20)"),
    ("Protein_name", "VARCHAR(500)"),
    ("Amino_acid_sequence", "TEXT"),
    ("PRIMARY KEY", "(Accession_No, Protein_id)"),
    ("FOREIGN KEY(Accession_No)", "REFERENCES Gene(Accession_No)")
]

codon_columns = [
    ("Codon_id", "INT PRIMARY KEY AUTO_INCREMENT"),
    ("Codon", "CHAR(3)"),
    ("Amacid", "CHAR(6)")
]

codonuage_per_chrom_columns = [
    ("CodonUsage_Chrom_id", "INT PRIMARY KEY AUTO_INCREMENT"),
    ("Amacid", "CHAR(6)"),
    ("Codon", "CHAR(3)"),
    ("Number", "INT"),
    ("per1000", "Decimal(10, 5)"),
    ("Fraction", "Decimal(10,5)"),
    ("Codon_id", "INT"),
    ("FOREIGN KEY(Codon_id)", "REFERENCES Codon(Codon_id)")
]

codonusage_per_entry_columns = [
    ("CodonUsage_entry_id", "INT PRIMARY KEY AUTO_INCREMENT"),
    ("Accession_No", "VARCHAR(20)"),
    ("Amacid", "CHAR(3)"),
    ("Codon", "CHAR(6)"),
    ("Number", "INT"),
    ("per1000", "Decimal(10,5)"),
    ("Fraction", "Decimal(10,5)"),
    ("Codon_id", "INT"),
    ("FOREIGN KEY(Accession_No)", "REFERENCES Protein(Accession_No)"),
    ("FOREIGN KEY(Codon_id)", "REFERENCES Codon(Codon_id)")
]

index_info = {
    'Gene': ("idx_Gene_AccessioNo", ['Gene_Identifier', 'Accession_No']),
    'Protein': ("idx_Protein_ProteinName", ['Protein_name']),
    'CodonUsage_per_Entry': ("idx_CondonUsagePerEntry_AccessionNo", ['Accession_No'])
}

tables = ['Gene', 'Protein', 'Codon', 'CodonUsage_per_chrom', 'CodonUsage_per_Entry']
columns_info = [gene_columns, protein_columns, codon_columns, codonuage_per_chrom_columns, codonusage_per_entry_columns]
