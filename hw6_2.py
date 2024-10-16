'''
1a. Download human proteins from RefSeq and compute amino-acid frequencies
for the (RefSeq) human proteome.
- Which amino-acid occurs the most? The least?
- Hint: access RefSeq human proteins in human.protein.fasta.gz
  from the course data-folder.
 
1b. Download human proteins from SwissProt and compute amino-acid
frequencies for the SwissProt human proteome.
- Which amino-acid occurs the most? The least?
- Hint: access UniProt XML format SwissProt human proteins from
  http://www.uniprot.org/downloads -> “Taxonomic divisions”
1c. How similar are the human amino-acid frequencies of in
RefSeq and SwissProt? 
- Which amino-acids show the biggest difference in frequency?
'''

import sys
import Bio.SeqIO
import gzip

    
def count_aa(records):
    aa_count = {}
    
    for seq_rec in records:
        sequence = seq_rec.seq.upper()
        keys = [aa for aa in set(sequence)]
        values = [sequence.count(aa) for aa in keys]
        aa_frequency = dict(zip(keys, values))
        #print('Count of each Amino Acid:', aa_frequency)

        for aa, count in aa_frequency.items():
            if aa not in aa_count:
                aa_count[aa] = 0
            
            aa_count[aa] += count
            sorted_count = dict(
            sorted(aa_count.items(), key=lambda p: p[1], reverse=True)
            )

    #print('List of Amino Acids:', sorted_count.keys())
    #print('Total Number of Amino Acids:', len(sorted_count))
    #print('Total Amino Acids:', sorted_count)
    return sorted_count


with gzip.open("human.protein.fasta.gz", mode='rt') as f:
    records = Bio.SeqIO.parse(f, 'fasta')
    sorted_refseq = count_aa(records)
    ref_most = list(sorted_refseq.keys())[0]
    ref_least = list(sorted_refseq.keys())[-1]

    print('Dict of Amino Acids from Refseq:', sorted_refseq)
    print('Total Number of Amino Acids:', len(sorted_refseq))
    print('AA occurs the most:', ref_most)
    print('AA occurs the least:', ref_least)

with gzip.open("uniprot_sprot_human.xml.gz", mode='rt') as f:
    records = Bio.SeqIO.parse(f, 'uniprot-xml')
    sorted_swiss = count_aa(records)
    swiss_most = list(sorted_swiss.keys())[0]
    swiss_least = list(sorted_swiss.keys())[-1]

    print('Dict of Amino Acids from Swissprot:', sorted_swiss)
    print('Total Number of Amino Acids:', len(sorted_swiss))
    print('AA occurs the most:', swiss_most)
    print('AA occurs the least:', swiss_least)
    
def maxdiff(sorted_refseq, sorted_swiss):
    all_aa = list(sorted_refseq.keys())+list(sorted_swiss.keys())
    aa_diff = {}

    for aa in all_aa:
        refseq = sorted_refseq.get(aa,0)
        swiss = sorted_swiss.get(aa,0)
        difference = abs(refseq - swiss)
        aa_diff[aa] = difference
    max_diff = max(aa_diff, key=aa_diff.get)
    return max_diff

print('Max different in AA:', maxdiff(sorted_refseq, sorted_swiss))

f.close()






