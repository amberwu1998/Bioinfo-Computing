##Download or copy-and-paste the DNA sequence of the Anthrax SASP gene
##from the anthrax_sasp.nuc file in the course data-directory.
##Treat the provided sequence as the sequence to be translated (no 5' UTR).
##Write a Python program to print answers to the following questions:


# Question 1 Does the SASP gene start with a Met codon?
SASP = 'TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG'
#testseq = 'ATGCCTTGAATGCAACTG'
codon = 'ATG'

def ans1():
    if SASP.startswith(codon):
        a = 'yes'
    else:
        a = 'no'
    return a

print('Does the SASP gene start with a Met codon?', ans1())


# Question 2 Does the SASP gene have a frame 1 Met codon? 
atgpos = SASP.find(codon)
print('Start codon position:', atgpos+1)

frame = (atgpos%3)+1

def ans2():
    if frame == 1:
        b = 'yes'
    else:
        b = 'no'
    return b

print('Does the SASP gene have a frame 1 Met codon?', ans2())


# Question 3 How many nucleotides in the SASP gene?
print('How many nucleotides in the SASP gene?', len(SASP))


# Question 4 How many amino-acids in the SASP protein?
aanumber = len(SASP)//3
print('How many amino-acids in the SASP protein?', aanumber)


# Question 5 What is the GC content (% G or C nucleotides) of the SASP gene?
gnumber = SASP.count('G')
cnumber = SASP.count('C')
ans5 = ((gnumber+cnumber)/len(SASP))*100
print('What is the GC content (% G or C nucleotides) of the SASP gene?', ans5, '%')


