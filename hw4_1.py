# Write a command-line program for
# computing the reverse complement of primer pairs

# open file
import sys
input_file = sys.argv[1]
f = open(input_file)


# Define reverse complement
def comp(nuc):
    nucleotides = 'ACGTacgtNn'
    complements = 'TGCAtgcaNn'
    i = nucleotides.find(nuc)
    if i >= 0:
        return complements[i]
    return nuc

def revcomp(primer):
    rc = ""
    for n in primer:
        rc = comp(n) + rc
    return rc



# Extract primer pairs from file and compute revese complement
for line in f:
    f_split = line.strip().split()[0:3]
    #print(f_split)
    f_split[0] = revcomp(f_split[0])
    f_split[1] = revcomp(f_split[1])
    #print(f_split)
    seq = ' '.join(f_split)
    print(seq)

f.close() 


