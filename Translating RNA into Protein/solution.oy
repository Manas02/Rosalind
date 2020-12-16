# Translating RNA into Protein 

table = {'UAC':'Y','UAU':'Y','UAA':'','UAG':'','UGC':'C','AUA':'I','AUC':'I','AUU':'I','AUG':'M','ACA':'T','ACC':'T','ACG':'T','ACU':'T','AAC':'N','AAU':'N','AAA':'K','AAG':'K','AGC':'S','AGU':'S','AGA':'R','AGG':'R','CUA':'L','CUC':'L','CUG':'L','CUU':'L','CCA':'P','CCC':'P','CCG':'P','CCU':'P','CAC':'H','CAU':'H','CAA':'Q','CAG':'Q','CGA':'R','CGC':'R','CGG':'R','CGU':'R','GUA':'V','GUC':'V','GUG':'V','GUU':'V','GCA':'A','GCC':'A','GCG':'A','GCU':'A','GAC':'D','GAU':'D','GAA':'E','GAG':'E','GGA':'G','GGC':'G','GGG':'G','GGU':'G','UCA':'S','UCC':'S','UCG':'S','UCU':'S','UUC':'F','UUU':'F','UUA':'L','UUG':'L','UGU':'C','UGA':'','UGG':'W'}
def rna_aa(sequence):
    seq = ''
    for n in range(0,len(sequence),3):
        if sequence[n:n+3] in table.keys():
            seq += table[sequence[n:n+3]]
    return seq

f = open('rosalind_prot.txt').read().strip('\n')
print(rna_aa(f))
