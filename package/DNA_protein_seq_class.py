import sys


class Sequence:

    # constructor
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()

    # getter and setter for id
    @property
    def id(self):
        return self._id 
    
    # the setter is here as an example
    """
    @id.setter
    def id(self, id):
        self._id = id
    """

    # getter and setter for seq
    @property
    def seq(self):
        return self._seq
    
    # the setter is here as an example
    """
    @seq.setter
    def seq(self, seq):
        self._seq = seq.upper()
    """

    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)
    
    
    def protein_translation (self):
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))
    
        #self.seq.upper() - already done above?
        translation = ''
        for start in range(0, len(self.seq)-2, 3):
            codon = self.seq[start:start+3]
            try: 
                aa = codon_table[codon]
            except KeyError:
                sys.exit(f'codon {codon} is not valid')
            translation += aa
        return (translation)
    

class protein_sequence:
    
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()

        # getter and setter for id
    @property
    def id(self):
        return self._id 
    
    # the setter is here as an example
    """
    @id.setter
    def id(self, id):
        self._id = id
    """

    # getter and setter for seq
    @property
    def seq(self):
        return self._seq
    
    # the setter is here as an example
    """
    @seq.setter
    def seq(self, seq):
        self._seq = seq.upper()
    """


    def hydrophobic(self):
        hydrophobic_aa = ['A', 'I', 'L', 'M', 'F','W', 'Y', 'V']
        c_sequence = []
        for A in self.seq:
            if A not in hydrophobic_aa:
                c_sequence.append(A)
            else: 
                continue
        hydro_content = (((len(self.seq) - len(c_sequence)) / len(self.seq)) * 100)
        return(c_sequence, hydro_content)
    
 



