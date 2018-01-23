def distance(strand_a, strand_b):
    """
    A function that, given two dna strands, finds the minimum hamming distance
    between those.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("The lengths of the strands are different. \
        Hamming distance between them cannot be defined.")
    dist = 0
    for idx, _ in enumerate(strand_a):
        if strand_a[idx] != strand_b[idx]:
            dist += 1
    return dist
