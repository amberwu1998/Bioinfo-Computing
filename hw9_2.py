'''
Added try/except to modules
'''

import MyDNAStuff_try as mys
import codon_table_try as ct
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



