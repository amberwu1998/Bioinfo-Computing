# Modify your DNA translation program to translate
# in each forward frame (1,2,3)

# Modify your DNA translation program to translate
# in each reverse (complement) translation frame too.

# Modify your translation program to handle 'N' symbols
# in the third position of a codon
# - If all four codons represented correspond to the same amino-acid,
#   then output that amino-acid.
# - Otherwise, output 'X'.

import sys
codon_table = sys.argv[1]
seq_file = sys.argv[2]
t = open(codon_table)
f = open(seq_file)
#print(t)

# Build a dictionary for lines in standard code
data = {}
for line in t:
    eachline = line.split()
    key = eachline[0]
    value = eachline[2]
    #print(key, value, eachline)
    data[key] = value
#print('dictionary for standard code:', data)
t.close()

# Simplified typing
aas = data['AAs']
st = data['Starts']
b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']        


# Build dictionary for amino acid codes
aa_table = {}
initial = {}
for i in range(len(aas)):
    codon = b1[i]+b2[i]+b3[i]
    aminoacid = aas[i]
    aa_table[codon] = aminoacid
    initial[codon] = (st[i] == 'M')
#print('dictionary for amino acid codes:', aa_table)
#print('dictionary for initial codon:', initial)


# Input Sequence
seq = ''.join(f.read().split())
print('input sequence:', seq)

# Reverse complement sequence
comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
def revcomp(seq):
    rc = ''
    for i in seq:
        i = i.upper()
        if i in comp:
            rc = comp[i] + rc
            #print(rc)
        else:
            rc = 'X' + rc
    return rc

rcseq = revcomp(seq)
print("Reverse complement sequence:", rcseq)

def translation(seq, frame):
    aaseq = []
    for i in range(frame,len(seq),3):
        triplets = seq[i:i+3]
        if len(triplets) == 3:
            #print('triplets:', triplets)
            if triplets[2] != 'N' and aa_table.get(triplets) is not None:
                aa = aa_table[triplets]
                #print("aa", aa)
            elif triplets[2] == 'N' and triplets[0] in 'ACGT' and triplets[1] in 'ACGT':
                possible_codon = [(triplets[:2] + nuc) for nuc in 'ACGT']
                possible_aa = set(aa_table[codon] for codon in possible_codon)
                #print('possible codon:', possible_codon)
                #print('possible aa:', possible_aa)
                if len(possible_aa) ==1:
                    aa = list(possible_aa)[0]
                else:
                    aa = 'X'
                #print('aa',aa)
            else:
                aa = 'X'
                #print('aa',aa)
         
            aaseq.append(aa)
    return ''.join(aaseq)


print('Frame1:', translation(seq,0))
print('Frame2:', translation(seq,1))
print('Frame3:', translation(seq,2))
print('Frame-1:', translation(rcseq,0))
print('Frame-2:', translation(rcseq,1))
print('Frame-3:', translation(rcseq,2))

f.close()

    
