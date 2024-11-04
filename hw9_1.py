'''
Demonstrate the use of these modules to translate an amino-acid sequence
in all six-frames with just a few lines of code.
The final result should look similar to Slide 10.
Your program should handle DNA sequence with N’s in it.
'''

import MyDNAStuff as mys
import codon_table as ct
import sys


if len(sys.argv) < 3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)

table = ct.read_codons_from_filename(sys.argv[1])
seq = mys.read_seq_from_filename(sys.argv[2])
#print(table)
#print(seq)

if ct.is_init(table,seq[:3]):
    print("Initial codon is a translation start codon")

for frame in (1,2,3):
    print("Frame",frame,"(forward):",ct.translate(table,seq,frame))

for revframe in (1,2,3):
    print(
        "Frame",revframe,"(reverse):",
        ct.translate(table,mys.revcomp(seq),
                     revframe))



