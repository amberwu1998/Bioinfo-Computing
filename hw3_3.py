# Extend your solution for Exercise 1 from Lecture 5
# to get its two PCR primers from the command-line.

import sys
forwardseq = sys.argv[1]
reverseseq = sys.argv[2]

def revcomp(seq):
    seq = seq.upper() # rule out lower case error
    nuc = 'ACGT'
    comp = 'TGCA'     # mark complement
    rev_comp = ''     # set empty string list to be filled
    for i in seq:
        if nuc.find(i) >=0: # if i is in nuc list, return its reverse complement
            rev_comp = comp[nuc.find(i)] + rev_comp
        else:         # if i is not in nuc list, return N
            rev_comp = 'N' + rev_comp
    return rev_comp
        
print(revcomp(forwardseq))
print(revcomp(reverseseq))
