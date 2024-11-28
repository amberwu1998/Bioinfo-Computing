'''
Convert your modules for DNA sequence and codons
to a codon_table and DNASeq class.
'''

class codon_table:
    def __init__(self):
        self.codon_table = codon_table

        
    def read(self,filename):
        data = {}
        t = open(filename)
        for line in t:
            eachline = line.split()
            key = eachline[0]
            value = eachline[2]
            data[key] = value
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
        self.codon_table = codon_table


    def amino_acid(self,codon):
        aa = self.codon_table[codon]['AA']
        return aa


    def is_init(self,codon):
        result = self.codon_table[codon]['Initial']
        return result

    
    def get_ambig_aa(self,codon):
        codon = codon.upper()
        if codon.find('N') == 2:
            possible_codon = [(codon[:2] + nuc) for nuc in 'ACGT']
            possible_aa = set(self.codon_table[codon]['AA']
                              for codon in possible_codon)

            if len(possible_aa) == 1:
                aa = list(possible_aa)[0]
            else:
                aa = 'X'
            
        else:
            aa = 'X'

        return aa


    def startswith_init(self,seq):
        codon = seq[:3]
        result = self.is_init(codon)
        return result


    
    def translate(self,seq,frame):
        aaseq = []
        for i in range(frame-1,len(seq),3):
            codon = seq[i:i+3]

            if len(codon) == 3:
                if 'N' in codon:
                    aa = self.get_ambig_aa(codon)
                else:
                    aa = self.amino_acid(codon)
                aaseq.append(aa)      
        return ''.join(aaseq)

'''
ds = codon_table()
ds.read('standard.code')
print(ds.is_init('ACT'))
print(ds.startswith_init('ACTGAATGCATG'))
print(ds.translate(seq='ATCGAACTAGNTA', frame=1))
'''




