# Copyright (c) 2018, Jenny Su
# See the LICENSE.txt for licensing information
#
# Database tier of implementation of a Chromosome (12) Browser
# MSc. Bioinformatics, Birkbeck & UCL - BioComputing II
# Taught by: Dr. Andrew C.R. Martin. UCL

import sys
import csv
import re
import json

import model
import db_API


def write_csvRow(filename, row, mode):

    with open(filename, mode) as f:
        writer = csv.writer(f)
        writer.writerow(row)


def parse_cdsIndexString(string):

    try:
        execludes = ["[<>:()]", 'complement']
        # li = [x.strip().split(":")[-1].replace("<", '').replace(">", '') for x in string.split(",")]
        li = [re.sub(r"%s" % '|'.join(execludes), '', x.strip().split(":")[-1]) for x in string.split(",")]
        li = [x.split("..") for x in li]
        li = [list(map(int, sublist)) for sublist in li]
    except:
        li = []

    return li


def get_min_max(li_of_lis):
    flat_list = [item for sublist in li_of_lis for item in sublist]

    return min(flat_list), max(flat_list)


def get_codonUsageResults(cds_sequence):

    results = []

    length_CDS = len(cds_sequence)
    number_residues = int(length_CDS/3)
    if number_residues == 0:
        return results

    for amacid in Amacid_Codon.keys():

        amacid_results = []
        amacid_codon_number = 0

        for codon in Amacid_Codon.get(amacid):
            number_codons = cds_sequence.count(codon.lower())

            _1000 = float(number_codons)*3/number_residues * 1000

            amacid_codon_number += number_codons

            amacid_results.append([amacid, codon, number_codons, _1000])

        if amacid_codon_number > 0:
            [x.append(float(x[2])/amacid_codon_number) for x in amacid_results]
            results.extend(amacid_results)

    return results


def main(geneBank_file):
    with open(geneBank_file) as f:
        raw_text = f.read()

    blocks = raw_text.split("LOCUS")

    allCds_sequence = ''
    for block in blocks[1:]:
        accession_nos = re.search(r"ACCESSION(.+)", block).group(1).strip().split(" ")

# Values of Gene.csv

        organism = re.search(r"ORGANISM(.+)", block).group(1).strip()

        if "/map" in block:
            chromosormal_location = re.search(r'/map=\"(.+?)\"', block).group(1).strip()
        else:
            chromosormal_location = ''

        if re.search(r"CDS\s+(complement\()*join", block):
            cds_index_string = re.search(
                r"CDS.+?join\((.+?)\)", block, flags=re.DOTALL).group(1).strip().replace("\n", '')
        else:
            cds_index_string = re.search(r"CDS\s+(.+)", block).group(1).strip()

        cds_index_list = parse_cdsIndexString(cds_index_string)

        if len(cds_index_list) > 0:
            cds_start, cds_end = get_min_max(cds_index_list)

        if "/gene" in block:
            gene_identifier = re.search(r'CDS.+?/gene=\"(.+?)\"', block, flags=re.DOTALL).group(1).strip()
        else:
            gene_identifier = ''

        dna_sequence = re.sub(
            r"\d+", '', re.search(r"ORIGIN(.+)", block, flags=re.DOTALL
                                  ).group(1).strip().replace("\n", '').replace(" ", '').replace("//", ''))

        cds_sequence = ''
        for cds_index in cds_index_list:
            cds_sequence = dna_sequence[cds_index[0]-1: cds_index[1]] + " "

        sequence_length = len(dna_sequence)

        for accession_no in accession_nos:
            gene_row = [
                accession_no,
                gene_identifier,
                chromosormal_location,
                organism,
                sequence_length,
                dna_sequence,
                cds_start,
                cds_end,
                cds_sequence
            ]

            db_API.insert_row('Gene', [x[0] for x in model.gene_columns], gene_row)
            # write_csvRow(gene_csv, gene_row, 'a')

#   Calculation for codon_usage_result.csv

        codonUsageResults = get_codonUsageResults(cds_sequence)
        for accession_no in accession_nos:
            # [x.insert(0, accession_no) for x in codonUsageResults]
            for codonUsageResult in codonUsageResults:
                codon_id = db_API.fetch_one(
                    'Codon', ['Codon_id'], {'Codon': codonUsageResult[1], 'Amacid': codonUsageResult[0]}).get('Codon_id')
                db_API.insert_row(
                    "CodonUsage_per_Entry", [x[0] for x in model.codonusage_per_entry_columns[:7]],
                    [accession_no]+codonUsageResult+[codon_id])
                # write_csvRow(codonUsageResult_csv, [accession_no]+codonUsageResult, 'a')

#   Values for protein.csv

        if '/protein_id=' in block:
            protein_id = re.search(r'/protein_id=\"(.+)\"', block).group(1).strip()
        else:
            protein_id = ''

        if '/product=' in block:
            protein_name = re.search(r'CDS.+?/product=\"(.+?)\"', block, flags=re.DOTALL).group(1).strip()
        else:
            protein_name = ''

        if '/translation=' in block:
            amino_acid_sequence = re.search(
                r'CDS.+?/translation=\"(.+?)\"', block, flags=re.DOTALL
            ).group(1).strip().replace("\n", "").replace(" ", '')
        else:
            amino_acid_sequence = ''

        for accession_no in accession_nos:
            protein_row = [accession_no, protein_id, protein_name, amino_acid_sequence]

            db_API.insert_row('Protein', [x[0] for x in model.protein_columns[:4]], protein_row)
            # write_csvRow(protein_csv, protein_row, 'a')

        allCds_sequence += cds_sequence + ' '

#   Calculation for codon_usage_result_per_whole_chromosome.csv

    index = 0
    allCodonUsageResults = get_codonUsageResults(allCds_sequence)
    for result in allCodonUsageResults:
        index += 1
        codon_id = db_API.fetch_one('Codon', ['Codon_id'], {'Codon': result[1], 'Amacid': result[0]}).get('Codon_id')
        db_API.insert_row(
            "CodonUsage_per_chrom", [x[0] for x in model.codonuage_per_chrom_columns[:-1]], [index]+result+[codon_id])
        # write_csvRow(codonUsageResultPerWholeChromosome_csv, result, 'a')


if __name__ == "__main__":
    geneBank_file = "chrom_CDS_12"

    Amacid_Codon = {'Ala': ['GCG', 'GCA', 'GCT', 'GCC'],
                    'Cys': ['TGT', 'TGC'],
                    'Asp': ['GAT', 'GAC'],
                    'Glu': ['GAG', 'GAA'],
                    'Phe': ['TTT', 'TTC'],
                    'Gly': ['GGG', 'GGA', 'GGT', 'GGC'],
                    'His': ['CAT', 'CAC'],
                    'Ile': ['ATA', 'ATT', 'ATC'],
                    'Lys': ['AAG', 'AAA'],
                    'Leu': ['TTG', 'TTA', 'CTG', 'CTA', 'CTT', 'CTC'],
                    'Met': ['ATG'],
                    'Asn': ['AAT', 'AAC'],
                    'Pro': ['CCG', 'CCA', 'CCT', 'CCC'],
                    'Gln': ['CAG', 'CAA'],
                    'Arg': ['AGG', 'AGA', 'CGG', 'CGA', 'CGT', 'CGC'],
                    'Ser': ['AGT', 'AGC', 'TCG', 'TCA', 'TCT', 'TCC'],
                    'Thr': ['ACG', 'ACA', 'ACC'],
                    'Val': ['GTG', 'GTA', 'GTT', 'GTC'],
                    'Trp': ['TGG'],
                    'Tyr': ['TAT', 'TAC'],
                    'End': ['TGA', 'TAG', 'TAA']
                    }


#   Create table and index
    db_API.create_tables(model.tables, model.columns_info)
    db_API.create_indexes(model.index_info)

#   Fill Codon table.
    id = 0
    for key in Amacid_Codon.keys():
        for codon in Amacid_Codon[key]:
            id += 1
            db_API.insert_row('Codon', [x[0] for x in model.codon_columns], [id, codon, key])


# Paring the raw text, calculate the values and insert into DB
    main(geneBank_file)

