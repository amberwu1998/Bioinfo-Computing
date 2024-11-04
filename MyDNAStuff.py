'''
Rework the lecture, and your solutions (or mine) from the Homeworks #1
through #4, to make a MyDNAStuff module.
- Put as many useful nucleotide functions as possible into the module...

'''

# get file
def read_seq_from_filename(seq_filename):
    seq_file = open(seq_filename)
    dna_seq = ''.join(seq_file.read().split())
    dna_seq = dna_seq.upper()
    seq_file.close()
    return dna_seq


#seq = 'AATATTAATGCAT'

# Define complement
def complement(seq):
    comp_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
    comp = ''.join(
        [comp_dict[nuc] for nuc in seq.upper()]
        )
    return comp
#print(complement(seq))


# Define reverse
def reverse(seq):
    seq = ''.join(reversed(seq))
    return seq
#print(reverse(seq))


# Define reverse complement
def revcomp(seq):
    comp_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
    rc = ''.join(
        [comp_dict.get(i)
         for i in reversed(seq.upper())]
        )
    return rc
#print(revcomp(seq))


# Test whether the sequence is a perfect tandem repeat
def tandem_repeat(seq):
    for i in range(1, (len(seq)//2)+1):
        if len(seq)%i == 0 and (len(seq)//i)*seq[0:i] == seq:
            print('The sequence is a perfect tandem repeat')
            return True
    print('The sequence is NOT a perfect tandem repeat')
    return False
#tandem_repeat(seq)


#Calculate GC count percentage
def gc_content(seq):
    g_count = seq.count('G')
    c_count = seq.count('C')
    return (g_count + c_count) / len(seq) * 100
#print(gc_content(seq))


