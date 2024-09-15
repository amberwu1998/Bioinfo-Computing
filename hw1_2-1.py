# Excercise 2
dna_sequence = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"
print(dna_sequence)
print(len(dna_sequence))
start_codon_position = dna_sequence.find('atg')
print(start_codon_position)
translation_frame = start_codon_position % 3+1
print(translation_frame)
