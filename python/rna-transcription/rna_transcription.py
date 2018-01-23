DNA_TO_RNA = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(dna_strand):
    """
    A function that, given a dna strand, returns rna transcription of it
    Raies ValueError with a meaningful message if the dna strand is invalid
    """
    try:
        return "".join([DNA_TO_RNA[dna_nucleotide] for dna_nucleotide in dna_strand])
    except KeyError as err:
        raise ValueError("{} is an invalid DNA Nucleotide".format(err))
