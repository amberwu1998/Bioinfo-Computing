# Write a command-line program for manipulating a DNA sequence

import sys
input_file = sys.argv[1]
function = sys.argv[2]
seq_input = ''. join(open(input_file).read().split())
print('The input sequence is:', seq_input)
#seq1 = 'AGGTaTCCG'

# define complement
def comp(seq):
    seq = seq.upper() 
    nucleotide = 'ACGT'
    complement = 'TGCA'     
    comp = ''   
    for i in seq:
        if nucleotide.find(i) >=0: 
            comp += complement[nucleotide.find(i)]
            # print(comp)
        else:         # if i is not in nuc list, return N
            comp += 'N'
            # print(comp)
    return comp


def rev(seq):
    seq = seq.upper()
    revseq = ''
    for i in seq:
        revseq = i + revseq
        # print(i, revseq)
    return revseq
  

def revcomp(seq):    
    rev_comp = comp(rev(seq))
    return rev_comp

def command():
    if function.lower() == 'complement':
        print('The Complement of the sequence is:', comp(seq_input))
    elif function.lower() == 'reverse':   
        print('The Reverse of the sequence is:', rev(seq_input))
    elif function.lower() == 'reversecomplement':
        print('The ReverseComplement of the sequence is:', revcomp(seq_input))
    else:
        print('Please enter the correct operation.')

command()


