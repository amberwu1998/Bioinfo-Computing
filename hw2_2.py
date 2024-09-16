# 2.1.1 Write a Python program to compute the reverse complement of a codon
codon = 'ATG'

first = codon[0]
second = codon[1]
third = codon[2]

reversed_codon = third + second + first

print("The input codon:",codon)
print("The codon reversed:",reversed_codon)

# 2.1.2 + 2.3 Add the “complement” function + handle upper and lower-case nucleotide
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

reversed_comp_codon = complement(reversed_codon[0])+complement(reversed_codon[1])+complement(reversed_codon[2])

print("The reverse complement of condon is:", reversed_comp_codon)


# 2.2 Place the reverse complement code in a new function

def reversecomp(codon_input):
    output = ''
    for nuc in codon_input:
        output = complement(nuc) + output
    return output

codon1 = 'AGTCCCATCAATGG'
codon2 = 'AaatGGACcttCGA'
codon3 = 'AAAAAAAAAAAAAAAAAAAAAAaaaaaa'

print('Reverse Complement Condon in One Run:', reversecomp(codon))
print('test run 1:', reversecomp(codon1))
print('test run 2:', reversecomp(codon2))
print('test run 3:', reversecomp(codon3))

























