"""
This module describes the API of the Chromosome 12 Browser
Implementation of the Browser as a Project of Biocomputing II

For the MSc. Bioinformatics, in Birkbeck College & UCL
Taught by: Dr. Andrew C.R. Martin, UCL

Copyright (c) 2018, Ioannis Valasakis <code@wizofe.uk>
See the LICENSE.txt for licensing information

Version 0.1b Beta ('Making it work')

Todo:
    * Finalise the testing

For more information about the API see doc/docs.md
For the essay doc/essay.pdf
"""

from database.db_API import *
from CUsage import *
from AlignSequence import *


def identify_coding_regions(dna):
    """ Wrapper of the database.db_API to return the coding regions
    of the input DNA sequence
    Args:
        DNA(str): The input DNA sequence
    Return:
        CDS(list): Coding Regions in the specified DNA sequence
    """
    return get_CDS(DNA)[4]

def generate_coding_sequence(dna):
    """ Wrapper of the database.db_API to return the joined coding sequence
    of the input DNA sequence
    Args:
        DNA(str): The input DNA sequence
    Return:
        cseq(str): DNA coding sequence
    """

    cseq = ""
    for cds in len(CDS):
        cseq.join(cds)

    return cseq

def count_codon_usage(gene):
    """
    Calculates the codon usage for a specified gene
    It can be used to calculate the usage either across a region or the whole
    See CUsage.py for the implementation of the Class

    Args:
        gene(str): Gene to calculate CDS
        codon_loc(int): The location of the codon
    Return:
        codon_count(float): CDS

    """
    cai = CodonAdaptationIndex(gene)
    codon_loc = getCDS(gene)[2:3]
    return cai._count_codons(codon_loc)


def align(dna, protein, matrix, gap_penalty):
    """ Implementation of a Waterman alignment
    See AlignSequence module for more

    Args:
        dna(str): given dna to be aligned
        protein(str): protein sequence to be aligned
        matrix(list): a lookup matrix input
        gap_penalty(int): the value of the required gap_penalty
    Return:
        alignment (list[list]): an array including a list of the alignments

    """
    return align_sequence(dna, protein, match_award=10, m_penalty=-5, gap_penalty=-5)

def identify_re_sites(self, dna, re_sites):
    """ Identify the restriction enzyme cut locations in the DNA
    Args:
        dna(str): DNA to calculate the RE cut locations
    Return:
        re_location(list): the location of the RE cut

    """
    start = 0
    end = len(dna)
    re_location = []
    while dna.find(re_sites,start,end) != -1 :
        x = dna.find(re_sites,start,end)
        re_location.append(x)
        start = x+1

    return re_location


def re_unique(dna, protein):
    """ Generate a list of the restriction enzyme sites of the DNA
    Args:
        dna(str): The requested dna
        (list): The location of the codon
    Return:
        found(list): unique CDS

    """
    found = None
    site = dna.find(protein)

    while site != -1:
        if found:
            break
        found = site
        site = dna.find(protein, found + 1)
    else:
        if found is not None:
            return found

def get_protein_info(self, protein):
    """ Database API wrapper to get the requested info for a specific protein
    Args:
        protein(str): ID of a protein
    Return:
        ac_number(int): protein accession number
        protein_id(int): the ID of the protein
        protein_name(str): the name of requested protein
        aa_seq(str): the aminoacid sequence of the requested protein
    """

    ac_number, protein_id, protein_name, aa_seq = getProinfo_name(protein)
    return ac_number, protein_id, protein_name, aa_seq
