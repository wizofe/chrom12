"""
This module is the TDD approach to testing and developing
the API of the Chromosome 12 Browser
Implementation of the Browser as a Project of Biocomputing II

For the MSc. Bioinformatics, in Birkbeck College & UCL
Taught by: Dr. Andrew C.R. Martin, UCL

Copyright (c) 2018, Ioannis Valasakis <code@wizofe.uk>
See the LICENSE.txt for licensing information

Version 0.1b Beta ('Making it work')

For more information about the API see doc/docs.md
For the essay doc/essay.pdf
"""

import unittest

class TestMainFunction(unittest.TestCase):
    """ Tests for the main function
    Each test is a function beginning with 'test_'
    """

    """ 
    Fake values for testing the stub
    """
    global dna
    dna = "ATCGCG"
    global protein_sequence
    protein_sequence = "AT"
    global dna_coding
    dna_coding = ""
    global re_sites
    re_sites = ""
    global gene
    gene = "ATT"
    global codon
    codon = "ATT"
    global info
    info = ""

    def test_identify_coding_regions_from_dna(self, dna):
        pass
    # Given in the genbank file - return: CDS location (int)

    def test_generate_coding_sequence_from_dna(self, dna):
        """ Description

        Args:
            one: this one

        Returns:
            This is it. True for success.
        """
        pass
        # join the dna sequence from location return: DNA sequence (str)

    def test_align_protein_seq_with_dna_coding(self, protein_sequence, dna_coding):
        pass
        # get protein sequence translation (from genbank =)
        # and align(function) with CDS return: alignment (str)

    def test_identify_re_sites(self, dna):
        pass
        # argument: list of RE's, DNA ATGCG
        # CGCATGCGACCCTTG
        # return: location e.g. 35..39 ATCGC (re)

    def test_provide_re_sites_list(self, re_sites):
        pass
        # return a list with RE sites to FE [list of strings]

    def test_identify_re_restriction_in_coding_region(self, re_sites):
        pass
        # aminoacid dictionary
        # return count usage: integer

    def test_count_codon_usage_in_gene(self, gene):
        pass

    def test_calculate_codon_usage_across_all_regions(self, codon):
        pass
        # store in a database or text file
        # return count usage in the CODING REGION (CDS)

    def test_extract_information_from_db(self, info):
        pass
        # Accession Number Genbank Protein
        # Keywords



