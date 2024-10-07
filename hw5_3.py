'''
Write a program to compute and output the frequency of each nucleotide
in a DNA sequence using a dictionary (see lec. 9).
Output the frequencies in most-occurrences to least-occurrences order.

'''

seq = 'aAAAAAARRQMMMCCGGGGGGGGGT'

def frequency(seq):
    seq = seq.upper()
    keys = [nuc for nuc in set(seq)]
    values = [seq.count(nuc) for nuc in keys]
    #print(keys, values)
    nuc_frequency = dict(zip(keys, values))
    sorted_frequency = dict(
        sorted(nuc_frequency.items(), key=lambda p: p[1], reverse=True)
        )
    return sorted_frequency

print('Sorted Frequency in a dictionary:', frequency(seq))

        
