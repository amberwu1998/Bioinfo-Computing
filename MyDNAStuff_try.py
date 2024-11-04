'''
Add some try/except blocks in your DNA modules from Exercise 16.1
'''

# get file
def read_seq_from_filename(seq_filename):
    try:
        seq_file = open(seq_filename)
        dna_seq = ''.join(seq_file.read().split())
        dna_seq = dna_seq.upper()
        seq_file.close()
        return dna_seq
    
    except FileNotFoundError:
        print(("Can't find the sequence file"))
        exit(1)

    except IndexError:
        print("Can't read the sequence file")
        exit(1)

#seq = 'AATATTAATGCAT'


# Define complement
def complement(seq):
    comp_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
    try:
        comp = ''.join(
            [comp_dict[nuc] for nuc in seq.upper()]
            )
        return comp
    
    except KeyError:
        print('Invalid sequence')
        exit(1)
    
    except AttributeError:
        print('Incorrect Type of Input')
        exit(1)
#print(complement([1,2]))


# Define reverse
def reverse(seq):
    seq = ''.join(reversed(seq))
    return seq
#print(reverse(seq))


# Define reverse complement
def revcomp(seq):
    comp_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
    try:
        rc = ''.join(
            [comp_dict.get(i)
             for i in reversed(seq.upper())]
            )
        return rc
    
    except KeyError:
        print('Invalid sequence')
        exit(1)
    
    except AttributeError:
        print('Incorrect Type of Input')
        exit(1)
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




