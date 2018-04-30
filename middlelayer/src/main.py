# Copyright (c) 2018, Ioannis Valasakis <code@wizofe.uk>
# See the LICENSE.txt for licensing information
#
# Middle layer implementation of a Chromosome (12) Browser
# MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
# Taught by: Dr. Andrew C.R. Martin. UCL

import unittest

class TestMainFunction(unittest.TestCase):
    """ Tests for the main function
    Each test is a function beginning with 'test_'
    """
    def test_identify_coding_regions_from_dna(self, dna):
        self.assertEqual(1, 1)

    def test_generate_coding_sequence_from_dna(self, dna):
        pass

    def test_align_protein_seq_with_dna_coding(self, protein_sequence, dna_coding):
        pass

    def test_identify_re_sites(self, dna):
        pass

    def test_provide_re_sites_list(self, re_sites):
        pass
    # return a list with RE sites to FE

    def test_identify_re_restriction_in_coding_region(self, re_sites):
        pass

    def test_count_codon_usage_in_gene(self, dna):
        pass

    def test_calculate_codon_usage_across_all_regions(self, codon):
        pass
    # store in a database or text file

    def test_extract_information_from_db(self, info):
        pass
    # may be wrappers to db code
    # complete gene list
    # or individual information


