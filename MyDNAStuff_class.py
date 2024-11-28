'''
Convert your modules for DNA sequence and codons to a codon_table
and DNASeq class.
'''

class DNASeq:
    def __init__(self,seq="",name=""):
        self.seq = seq
        self.name = name

        
    def read(self,filename):
        seq_file = open(filename)
        dna_seq = ''.join(seq_file.read().split())
        dna_seq = dna_seq.upper()
        seq_file.close()
        
        self.seq = dna_seq
        
    def reverse(self):
        return ''.join(reversed(self.seq))

    
    def complement(self):
        comp_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
        comp = ''.join(
            [comp_dict[nuc] for nuc in self.seq.upper()]
            )
        return comp

    
    def reverseComplement(self):
        return ''.join(reversed(self.complement()))

    
    def length(self):
        return len(self.seq)

    
    def freq(self,nuc):
        return self.seq.count(nuc)

    
    def percentGC(self):
        gccount = self.freq('C') + self.freq('G')
        return 100*float(gccount)/self.length()

    
    def __str__(self):
        asstr = ">"+self.name+"\n"+self.seq
        return asstr


