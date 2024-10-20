'''
Starting with the program of slide 19 and working with
BAM file 10_Normal_Chr21.bam,  find the locus with:
- Single diploid-organism heterozygosity (approx.), and highest coverage
- Output the locus, its alleles, and the number of high-quality reads
  for each allele.
  
Then, add the code to filter out bad/poor alignments (slide 20)
to your program.
- Does the highest coverage heterozygous locus and its read counts change?
  If so, how?
'''

import pysam
bf = pysam.Samfile('10_Normal_Chr21.bam')

max_coverage = 0
max_locus = None
max_alleles = {}

# For every position in the reference
for pileup in bf.pileup('21'):
    counts = {}
    # ...examine every aligned read
    for pileupread in pileup.pileups:

        if pileupread.indel:
            continue
        if pileupread.is_del:
            continue
        al = pileupread.alignment
        if al.is_unmapped:
            continue
        if al.is_secondary:
            continue
        if int(al.opt('NM')) > 1:
            continue
        if int(al.opt('NH')) > 1:
            continue

        #get the read base
        if not pileupread.query_position:
            continue
        
        readbase = pileupread.alignment.seq[pileupread.query_position]
        # Count the number of each base
        if readbase not in counts:
            counts[readbase] = 0
        counts[readbase]+= 1
        
    coverage = pileup.n    
    # If there is no variation, move on
    if len(counts) < 2:
        continue
    if sorted(counts.values())[-2] < 10:
        continue
    if coverage > max_coverage:
        max_coverage = coverage
        max_locus = pileup.pos
        max_alleles = counts
    # Otherwise, output the position, coverage and base counts

print('Locus with max coverage:', max_locus)
print('Max Coverage:', max_coverage)

for base, count in sorted(max_alleles.items()):
    print('Allele:', base, 'Allele Count:', count)
    
    

