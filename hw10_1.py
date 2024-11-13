'''
Demonstrate the use of this module and the codon table module to translate
an amino-acid sequence in all six-frames with just a few lines of code.
-- Hint: just import the new classes from their module(s) and call
    the necessary methods/functions!

'''

from MyDNAStuff_class import *
from codon_table_class import *
import sys

if len(sys.argv) < 3:
    print("Require codon table and", \
          "DNA sequence on command-line.")
    sys.exit(1)

codons = codon_table()
codons.read(sys.argv[1])

seqs = DNASeq()
seqs.read(sys.argv[2])
#print(seqs.seq)

if codons.startswith_init(seqs.seq):
    print("Initial codon")


for frame in (1,2,3):
    print("Frame",frame,"(forward):",codons.translate(seqs.seq,frame))


for revframe in (1,2,3):
    print(
        "Frame",revframe,"(reverse):",
        codons.translate(seqs.reverseComplement(),
                     revframe))

