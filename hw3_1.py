# Write a program to compute the reverse complement sequence of
# both the forward and reverse primer (in one program)

# Input
mapk = 'CGGTGTCAATGGTTTGGTGC' # Forward seq
rev_mapk = 'GACGATGTTGTCGTGGTCCA' # Reverse seq

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
        
print(revcomp(mapk))
print(revcomp(rev_mapk))
