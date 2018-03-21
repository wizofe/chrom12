def gene_info():
"""Get the gene information for a specific gene search"""
gene_info=cur.execute("SELECT * FROM Gene WHERE 'identifier_info from middle layer'")
gene_result = cur.fetchone()
return gene_result (as tuple)  


def protein_info():
"""Get the protein information for a specific gene search"""
protein_info=cur.execute("SELECT * FROM Protein WHERE ‘identifier_info from middle layer'")
protein_result = cur.fetchone()
return protein_result (as tuple) 


def get_CDS (start, end, DNA sequence)
"""Generate the coding DNA sequence from the DNA"""
Return  CDS (as dict)


def get_CodonUsage_entry():
"""Get the codon usage info for a specific gene search"""
Usage_info =cur.execute("SELECT * FROM CodonUsage_Per_Entry JOIN Codon on CodonUsage_Per_Entry.condon_ID=codon.condon_ID WHERE Accession_No.= ‘from middle layer’”)
usage_result = cur.fetchone()
return usage_result (as tuple) 


def get_CodonUsage_Chrom12():
"""Get the overall codon usage frequencies in the whole chromosome 12"""
get_usage=cur.execute("SELECT * FROM CodonUsage_Per_Chrom12 JOIN Codon on CodonUsage_Per_Chrom12.condon_ID=codon.condon_ID)
usage_data = cur.fetchall()
return usage_data (as tuple)
