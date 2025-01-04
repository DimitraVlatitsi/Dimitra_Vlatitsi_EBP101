#Find Gene Function that finds genes in files
#This code uses dna.seq file
#For other files change the file name
 
def find_genes(seq):
  stop_codons = ["TAA","TGA","TAG"]
  seq_len = len(seq)
  count = 0
  gene_num = 1
  print("If we have a sequence with 5->3 direction :")
  for i in range(seq_len - 2):
    if seq[i:i+3] == 'ATG':
      for j in range( i+3, seq_len - 2, 3 ):
        codon = seq[ j:j+3 ]
        if codon in stop_codons:
          count += 1
          gene = seq[ i:j+3 ]
          print(f'{gene_num}. {gene}')
          gene_num += 1
          break
  print(f'Number of possible genes : {count}')
  rev_seq = seq[ ::-1 ]
  rev_seq_len = len( rev_seq )
  rev_count = 0
  rev_gene_num = 1
  print("If we have a sequence with 3->5 direction :")
  for i in range( rev_seq_len - 2 ):
    if rev_seq[ i:i+3 ] == 'ATG':
      for j in range( i+3, rev_seq_len - 2, 3 ):
        codon = rev_seq[ j:j+3 ]
        if codon in stop_codons:
          rev_count += 1
          rev_gene = rev_seq[ i:j+3 ]
          print(f'{rev_gene_num}. {rev_gene}')
          rev_gene_num += 1
          break
  print(f'Number of possible genes : {rev_count}')

#Reads the file you want to use

def read_sequence_from_file(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip()  

# The file must contain a DNA sequence with capital letters, and no spaces or other symbols
#If the file is not in that form, it must be preprocessed

if __name__ == "__main__":
    file_name = "dna.seq"  
    sequence = read_sequence_from_file(file_name)
    find_genes(sequence)

