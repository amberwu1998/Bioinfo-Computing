'''
Rework the lecture, and your solutions (or mine) from Homework #5
to make the codon_table module with functions specified in this lecture.

'''

# Read file from standard.code and output codon table
def read_codons_from_filename(codonfile):
    data = {}
    t = open(codonfile)
    for line in t:
        eachline = line.split()
        key = eachline[0]
        value = eachline[2]
        #print(key, value, eachline)
        data[key] = value
    #print('dictionary for standard code:', data)
    t.close()
    
    codon_table = {}
    aas = data['AAs']
    st = data['Starts']
    b1 = data['Base1']
    b2 = data['Base2']
    b3 = data['Base3'] 
    for nuc in range(len(aas)):
        codon = b1[nuc]+b2[nuc]+b3[nuc]
        init = st[nuc]
        codon_table[codon] = {'AA': aas[nuc], 'Initial': init == 'M'} 
    return codon_table

#codon_table = read_codons_from_filename(codonfile)
#print(codon_table)


# Output Amino Acid from codon table
def amino_acid(table,codon):
    aa = table[codon]['AA']
    return aa
#print(amino_acid(codon_table, 'TTT'))



# Output initial from codon table
def is_init(table,codon):
    init = table[codon]['Initial']
    return init
#print(is_init(codon_table,'TTT'))


# Output Ambigous('X') when 'N' exists in codon
def get_ambig_aa(table,codon):
    codon = codon.upper()
    if codon.find('N') == 2:
        possible_codon = [(codon[:2] + nuc) for nuc in 'ACGT']
        possible_aa = set(table[codon]['AA'] for codon in possible_codon)
        #print(possible_codon)
        #print(possible_aa)
        if len(possible_aa) == 1:
            aa = list(possible_aa)[0]
        else:
            aa = 'X'
        
    else:
        aa = 'X'

    return aa
#print(get_ambig_aa(codon_table,'TCN'))



# Translate the sequence into AA chain
def translate(table,seq,frame):
    aaseq = []
    for i in range(frame-1,len(seq),3):
        codon = seq[i:i+3]
        #print(codon)
        if len(codon) == 3:
            if 'N' in codon:
                aa = get_ambig_aa(table,codon)
            else:
                aa = amino_acid(table,codon)
            aaseq.append(aa)      
    return ''.join(aaseq)
#print(translate(codon_table,'TTNCCTATANA',3))



