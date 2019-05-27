"""
Take DNA from file and outputs dictionary with count of species in the DNA.

@author: Jaanus Keller
"""


def read_dna_data_from_file(filename):
    """
    Acquire DNA from file and remove endlines.

    Argument:
    filename -- string with the exact name of the file

    Returns:
    dna as a string
    """
    dna = ""
    with open(filename) as file:
        for line in file:
            dna += line.strip()
    return dna


def transcribe_dna_to_rna(dna):
    """
    Change DNA into RNA.

    Argument:
    dna -- string of dna containing A, T, G and/or C

    Returns:
    rna as a string
    """
    rna = ""
    correct_values = 'ATCG'
    if dna == '':
        return None
    for letter in dna:
        if letter not in correct_values:
            return None
        if letter == 'A':
            rna += 'U'
        if letter == 'T':
            rna += 'A'
        if letter == 'G':
            rna += 'C'
        if letter == 'C':
            rna += 'G'
    return rna


def translate_rna_to_protein(rna):
    """
    Change RNA into protein.

    Argument:
    rna -- string of rna containing A, U, G and/or C

    Returns:
    protein made from 3 element RNA pieces
    """
    proteins = {
        'A': ['GCU', 'GCC', 'GCA', 'GCG'],
        'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'N': ['AAU', 'AAC'],
        'D': ['GAU', 'GAC'],
        'C': ['UGU', 'UGC'],
        'Q': ['CAA', 'CAG'],
        'E': ['GAA', 'GAG'],
        'G': ['GGU', 'GGC', 'GGA', 'GGG'],
        'H': ['CAU', 'CAC'],
        'I': ['AUU', 'AUC', 'AUA'],
        'Met': ['AUG'],
        'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
        'K': ['AAA', 'AAG'],
        'F': ['UUU', 'UUC'],
        'P': ['CCU', 'CCC', 'CCA', 'CCG'],
        'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
        'T': ['ACU', 'ACC', 'ACA', 'ACG'],
        'W': ['UGG'],
        'Y': ['UAU', 'UAC'],
        'V': ['GUU', 'GUC', 'GUA', 'GUG'],
        'Stop': ['UAA', 'UGA', 'UAG']
        }
    protein = ""
    correct_values = 'AUCG'
    if rna == '' or rna is None:
        return None
    for letter in rna:
        if letter not in correct_values:
            return None
    for i in range(0, len(rna) + 3, 3):
        gene = rna[i:i+3]
        for key in proteins:
            if gene in proteins[key]:
                protein += key
    return protein


def determine_species(classification_file):
    """
    Use file to count how often they appear.

    Argument:
    classification_file -- a file containing name of a species with their protein identifier

    Returns:
    dictionary with the name of the species and how many times it appears in the original DNA list
    """
    protein = translate_rna_to_protein(transcribe_dna_to_rna(read_dna_data_from_file('EX05_DNA.txt')))
    temp = []
    species = []
    dictionary = {}
    with open(classification_file) as file:
        for line in file:
            temp.append(line.strip())
    temp.pop(0)
    temp = list(set(temp))
    for collection in temp:
        species.append(collection.split(','))
    # make all species in the classification file have a count of 0
    for i in range(len(species)):
        dictionary[species[i][1]] = 0
    # count the times species exists in DNA
    for n in range(len(species)):
        for i in range(len(protein)):
            if species[n][2] in protein[i:i+len(species[n][2])]:
                dictionary[species[n][1]] += 1
    # remove species that were not in given DNA list from dictionary
    for i in range(len(species)):
        if dictionary[species[i][1]] == 0:
            del dictionary[species[i][1]]
    return dictionary

print(read_dna_data_from_file('EX05_DNA.txt'))
print()
print(transcribe_dna_to_rna(read_dna_data_from_file('EX05_DNA.txt')))
print()
print(translate_rna_to_protein(transcribe_dna_to_rna(read_dna_data_from_file('EX05_DNA.txt'))))
print()
print(determine_species('EX05_Protein.csv'))
