import re

# IMPORT regular expression module
# ASSIGN the given RNA sequence string to variable 'seq'
# USE regex to find all ORFs starting with AUG and ending at first stop codon (UAA/UAG/UGA)
# FIND the longest ORF from the matched list
# CALCULATE the length of the longest ORF
# PRINT the longest ORF and its length

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
orf=re.findall(r'AUG.+?(?:UAA|UAG|UGA)',seq)
largest_orf=max(orf,key=len)
largest_orf_lens=len(largest_orf)
print(f'largest ORF:{largest_orf}, length: {largest_orf_lens}   ')
