# Write a program to testwhether a PCR primer
# is a reverse complement palindrome.

seq1 = 'TTGAGTAGACGCGTCTACTCAA'
seq2 = 'TTGAGTAGACGTCGTCTACTCAA'
seq3 = 'ATATATATATATATAT'
seq4 = 'ATCTATATATATGTAT'
seq5 = 'ACt'

# define complement
def comp(nuc):
    nuc = nuc.upper()
    nucleotide = 'ATCG'
    complement = 'TAGC'
    i = nucleotide.find(nuc)
    if i >=0:
        comp = complement[i]
    else:
        comp = 'X'
    return comp
    
# define palindrome sequence based on sequence length
def pal(seq):
    forwardseq = ''
    reverseseq = ''
    for i in range(len(seq)//2):
        forwardseq += seq[i]
        reverseseq = comp(seq[i]) + reverseseq
        if len(seq)%2 == 0: #if sequence length is even
            palseq = forwardseq + reverseseq
            print(forwardseq, reverseseq, palseq) 
        else:               #if sequence length is odd
            palseq = forwardseq + seq[len(seq)//2] + reverseseq
            # print(forwardseq, seq[len(seq)//2], reverseseq, palseq)
    return palseq


# test reverse complement palindrome
def revcomppal(seq):
    seq = seq.upper()
    if seq == pal(seq):
        return True
    return False

print(revcomppal(seq3))
