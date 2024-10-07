'''
Write a reverse complement function (and package it up as a program)
as compactly as possible (1-2 lines), using the techniques introduced today.
Hint: Use a dictionary for complement, reversed on the sequence,
list comprehension to apply the get method of the dictionary,
and the join method for strings. 

'''


seq = 'aaCGGTAN'

def revcomp(seq):
    rc = ''.join(
        [{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}.get(i) for i in reversed(seq.upper())]
        )
    return rc

print('Reverse complement Sequence:', revcomp(seq))

