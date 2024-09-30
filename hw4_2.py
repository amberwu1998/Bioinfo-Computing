# Using just the concepts introduced so far,
# find as many (different!) ways as possible to
# code DNA reverse complement (at least 3!)


# Method 1
def complement(nuc):
    if nuc == 'A' or nuc =='a':
        comp = 'T'
    elif nuc == 'T' or nuc =='t':
        comp = 'A'
    elif nuc == 'G' or nuc =='g':
        comp = 'C'
    elif nuc == 'C' or nuc =='c':
        comp = 'G'
    else:
        comp = nuc
    return comp

def revcomp (seq):
    rc = ''
    for i in seq:
        rc = complement(i)+ rc
    return rc
#print(revcomp('AGT'))


# Method 2
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
#print(revcomp('ACC'))



# Method 3
comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
#print(comp['A'])
#print(comp.keys())
#print(comp.values())
#print(comp.items())

def revcomp(seq):
    rc = ''
    for i in seq:
        if i.upper() in comp:
            rc = comp[i] + rc
            print(rc)
        else:
            rc = 'X' + rc
    return rc

print(revcomp('ACGGARRT'))
        
    







