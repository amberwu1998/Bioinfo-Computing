# 3.1 program to test perfect tandem repeat
seq1 = 'AAAAAAAAAAAAAAAA'
seq2 = 'CACACACACACACAC'
seq3 = 'ATTCGATTCGATTCG'
seq4 = 'GTAGTAGTAGTAGTA'
seq5 = 'TCAGTCACTCACTCAG'

seq6 = 'AACAACAAC'
seq7 = 'AA'


def repeat(seq):
    for i in range(1, (len(seq)//2)+1):
        if len(seq)%i == 0 and (len(seq)//i)*seq[0:i] == seq:
            return True
    return False

print(repeat(seq6))

print(repeat(seq2))
print(repeat(seq5))

print(repeat(seq1))
print(repeat(seq3))
print(repeat(seq4))
