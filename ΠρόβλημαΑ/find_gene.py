#Definition of a function that finds genes in a sequence two-way with a given DNA sequence

def find_genes(seq):
  stop_codons = ["TAA","TGA","TAG"] #Def stop codons
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

find_genes("ACTAGATGCATACGCATCAATTAGCTACGTATCGTCAGTAAGTATGACTAGTCATGCTAGCTAGCTACTATCAGGAAGATTGTATTCATAGG")
