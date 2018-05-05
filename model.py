# Copyright (c) 2018, Jenny Su
# See the LICENSE.txt for licensing information
#
# Database tier of implementation of a Chromosome (12) Browser
# MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
# Taught by: Dr. Andrew C.R. Martin. UCL


gene_columns = [
    ("Accession_No", "VARCHAR(20) PRIMARY KEY"),
    ("Gene_Identifier", "VARCHAR(200)"),
    ("Chromosomal_location", "VARCHAR(200)"),
    ("Organism", "VARCHAR(20)"),
    ("Sequence_Length", "INT"),
    ("DNA_Sequence", "LONGBLOB"),
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
    ("per1000", "Decimal"),
    ("Fraction", "Decimal"),
    ("Codon_id", "INT"),
    ("FOREIGN KEY(Codon_id)", "REFERENCES Codon(Codon_id)")
]

codonusage_per_entry_columns = [
    ("Accession_No", "VARCHAR(20) PRIMARY KEY"),
    ("Amacid", "CHAR(3)"),
    ("Codon", "CHAR(6)"),
    ("Number", "INT"),
    ("per1000", "Decimal"),
    ("Fraction", "Decimal"),
    ("Codon_id", "INT"),
    # ("CodonUsage_Chrom_id", "INT"),
    ("FOREIGN KEY(Accession_No)", "REFERENCES Protein(Accession_No)"),
    ("FOREIGN KEY(Codon_id)", "REFERENCES Codon(Codon_id)"),
    # ("FOREIGN KEY(CodonUsage_Chrom_id)", "REFERENCES CodonUsage_per_chrom(CodonUsage_Chrom_id)")
]

index_info = {
    'Gene': ("idx_Gene_AccessioNo", ['Gene_Identifier', 'Accession_No']),
    'Protein': ("idx_Protein_ProteinName", ['Protein_name']),
    'CodonUsage_per_Entry': ("idx_CondonUsagePerEntry_AccessionNo", ['Accession_No'])
}

tables = ['Gene', 'Protein', 'Codon', 'CodonUsage_per_chrom', 'CodonUsage_per_Entry']
columns_info = [gene_columns, protein_columns, codon_columns, codonuage_per_chrom_columns, codonusage_per_entry_columns]



# gene_csv = "Genes.csv"
# protein_csv = "Proteins.csv"
# codonUsageResult_csv = "codon_usage_result.csv"
# codonUsageResultPerWholeChromosome_csv = "codon_usage_result_per_whole_chromosome.csv"
#
# gene_csv_header = [
#     'Accession_No',
#     'Gene_Identifier',
#     'Chromosomal_Location',
#     'Organism',
#     'Sequence_Length',
#     'DNA_Sequence',
#     'CDS_start',
#     'CDS_end',
#     'CDS_sequence'
# ]
#
# protein_csv_header = [
#     'accession_no',
#     'protein_id',
#     'protein_name',
#     'amino_acid_sequence'
# ]
#
# codonUsageResult_csv_header = [
#     'Accession_No',
#     'Amacid',
#     'Codon',
#     'Number',
#     '/1000',
#     'Fraction',
# ]
#
# codonUsageResultPerWholeChromosome_csv_header = [
#     'Amacid',
#     'Codon',
#     'Number',
#     '/1000',
#     'Fraction',
# ]
#
# write_csvRow(gene_csv, gene_csv_header, 'w')
# write_csvRow(protein_csv, protein_csv_header, 'w')
# write_csvRow(codonUsageResult_csv, codonUsageResult_csv_header, 'w')
# write_csvRow(codonUsageResultPerWholeChromosome_csv, codonUsageResultPerWholeChromosome_csv_header, 'w')

