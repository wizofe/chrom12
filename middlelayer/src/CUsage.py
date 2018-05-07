import math

"""
DNA Codon Table
Source: 1. https://en.wikipedia.org/wiki/DNA_codon_table
        2. http://www.cbs.dtu.dk/courses/27619/codon.html
"""
CodonsDict = {
    'ACT': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0, 'GCT': 0,
    'GCC': 0, 'GCA': 0, 'GCG': 0, 'TGT': 0, 'TGC': 0,
    'AAC': 0, 'AAA': 0, 'AAG': 0, 'GAT': 0, 'GAC': 0,
    'CGG': 0, 'AGT': 0, 'AGC': 0, 'AGA': 0, 'AGG': 0,
    'CTC': 0, 'CTA': 0, 'CTG': 0, 'ATT': 0, 'ATC': 0,
    'ATA': 0, 'ATG': 0, 'GTT': 0, 'GTC': 0, 'GTA': 0,
    'GTG': 0, 'TAT': 0, 'TAC': 0, 'TAA': 0, 'TAG': 0,
    'CAT': 0, 'CAC': 0, 'CAA': 0, 'CAG': 0, 'AAT': 0,
    'GAA': 0, 'GAG': 0, 'TCT': 0, 'TCC': 0, 'TCA': 0,
    'TCG': 0, 'CCT': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0,
    'TGA': 0, 'TGG': 0, 'CGT': 0, 'CGC': 0, 'CGA': 0,
    'TTT': 0, 'TTC': 0, 'TTA': 0, 'TTG': 0, 'CTT': 0,
    'GGT': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0}


SCodons = {
    'LEU': ['TTA', 'TTG', 'CTC', 'CTT', 'CTG', 'CTA'],
    'ASP': ['GAT', 'GAC'],
    'MET': ['ATG'],
    'ASN': ['AAC', 'AAT'],
    'PRO': ['CCT', 'CCG', 'CCA', 'CCC'],
    'LYS': ['AAG', 'AAA'],
    'STOP': ['TAG', 'TGA', 'TAA'],
    'THR': ['ACC', 'ACA', 'ACG', 'ACT'],
    'PHE': ['TTT', 'TTC'],
    'ALA': ['GCA', 'GCC', 'GCG', 'GCT'],
    'GLY': ['GGT', 'GGG', 'GGA', 'GGC'],
    'ILE': ['ATC', 'ATA', 'ATT'],
    'HIS': ['CAT', 'CAC'],
    'ARG': ['CGA', 'CGC', 'CGG', 'CGT', 'AGG', 'AGA'],
    'TRP': ['TGG'],
    'VAL': ['GTA', 'GTC', 'GTG', 'GTT'],
    'GLN': ['CAA', 'CAG'],
    'GLU': ['GAG', 'GAA'],
    'CYS': ['TGT', 'TGC'],
    'SER': ['TCT', 'TCG', 'TCA', 'TCC', 'AGC', 'AGT'],
    'TYR': ['TAT', 'TAC']}


class CodonAdaptationIndex(object):
    """A codon adaptation index (CAI) implementation

    CAI is the geometric mean of the weight associated to each codon over the length of the
    gene sequence (measured in codons). For more see: Sharp and
    Li (Nucleic Acids Res. 1987 Feb 11;15(3):1281-95).

    codes: only the synonymous codons in the standard table are considered.
    """

    def __init__(self):
        """Initialize the codon class."""
        self.index = {}
        self.codon_count = {}

    # use this method with predefined CAI index
    def set_cai_index(self, index):
        """Sets up an index to be used when calculating CAI for a gene.
        """
        self.index = index

    def generate_index(self, codon_loc):
        """Generate a codon usage index from an entry in our local database of CDS sequences.

        Argument:
            codon_loc: location of a codon containing CDS sequences

        Returns:
            CUI
        """
        # ensure that index is unique:
        if self.index != {} or self.codon_count != {}:
            raise ValueError("index has already been set or a codon count "
                             "has been performed. try with a new location.")

        # count codon occurrences in the file.
        self._count_codons(codon_loc)

        # now to calculate the index we first need to sum the number of times
        # synonymous codons were used all together.
        for cd in SCodons:
            total = 0.0
            # RCSU values are CodonCount/((1/num of synonymous codons) * sum of
            # all synonymous codons)
            rcsu = []
            codons = SCodons[cd]

            for codon in codons:
                total += self.codon_count[codon]

            # calculate the RSCU value for each of the codons
            for codon in codons:
                dm = float(total) / len(codons)
                rcsu.append(self.codon_count[codon] / dm)

            # calculate index W=RCSUi/RCSUmax:
            rcsu_max = max(rcsu)
            for codon_index, codon in enumerate(codons):
                self.index[codon] = rcsu[codon_index] / rcsu_max

    def cai_for_gene(self, dna_sequence):
        """Calculate the CAI for the provided DNA sequence.

        Arguments:
            dna_sequence(str): The DNA sequence in a string format

        Returns:
            cai_value(float): CAI for the input DNA sequence
        """
        cai_value, cai_length = 0, 0

        if dna_sequence.islower():
            dna_sequence = dna_sequence.upper()

        for i in range(0, len(dna_sequence), 3):
            codon = dna_sequence[i:i + 3]
            if codon in self.index:
                # ATG and TGG == 1:
                if codon not in ['ATG', 'TGG']:
                    cai_value += math.log(self.index[codon])
                    cai_length += 1
            # some indices may not include stop codons:
            elif codon not in ['TGA', 'TAA', 'TAG']:
                raise TypeError("not accepted codon in sequence: %s.\n%s"
                                % (codon, self.index))

        return math.exp(cai_value / (cai_length - 1.0))

    def _count_codons(self, codon_loc):
        # make the codon dictionary local
        self.codon_count = CodonsDict.copy()

        # iterate over sequence and count all the codons in the input codon location.
        for cur_record in codon_loc:
            # make sure the sequence is lower case
            if str(cur_record.seq).islower():
                dna_sequence = str(cur_record.seq).upper()
            else:
                dna_sequence = str(cur_record.seq)
            for i in range(0, len(dna_sequence), 3):
                codon = dna_sequence[i:i + 3]
                if codon in self.codon_count:
                    self.codon_count[codon] += 1
                else:
                    raise TypeError("not accepted codon %s in gene: %s"
                                    % (codon, cur_record.id))
