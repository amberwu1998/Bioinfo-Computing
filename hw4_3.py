# Write a program that takes a codon table file (standard.code)
# and a file containing nucleotide sequence (anthrax_sasp.nuc)
# as command-line arguments, and outputs the amino-acid sequence.


# Retrieve the files
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



# Extract triplets from sequence
seq = ''.join(f.read().split())
#print('input sequence:', seq)
aaseq = []
for i in range(0,len(seq),3):
    triplets = seq[i:i+3]
    aa = aa_table[triplets]
    aaseq.append(aa)
aaseq = ''.join(aaseq)
#print('amino acid chain:', aaseq)

f.close()



# Test initial codon consistency
if initial[seq[0:3]]:
    print('the initial codon is a valid translation start site')
else:
    print('the initial codon is NOT ca valid translation start site')
#print(seq[0:3], initial[seq[0:3]])
    






