def DNA_strand(dna):
    x = {
        'G': 'C',
        'C': 'G',
        'A': 'T',
        'T': 'A'
    }

    return ''.join([x[l] for l in dna])