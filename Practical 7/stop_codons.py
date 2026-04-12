import re
# FUNCTION read_fasta(file):
#     CREATE empty dictionary gene_dict
#     SET gene_name = None
#     SET gene_seq = empty string
#     OPEN file in read mode
#     FOR each line in the file:
#         REMOVE leading/trailing whitespace from line
#         IF line is empty:
#             SKIP this line
#         IF line starts with ">":
#             IF gene_name is not None AND gene_seq is not empty:
#                 ADD gene_name and gene_seq to gene_dict
#             EXTRACT gene name from line using regex "gene:(\S+)"
#             IF gene name is found:
#                 gene_name = extracted name
#             ELSE:
#                 gene_name = None
#             RESET gene_seq to empty string
#         ELSE:
#             IF gene_name is not None:
#                 APPEND line to gene_seq
#     AFTER processing all lines:
#         IF gene_name is not None AND gene_seq is not empty:
#             ADD gene_name and gene_seq to gene_dict
#     RETURN gene_dict
def read_fasta(file):
    gene_dict={}
    gene_name=None
    gene_seq=''
    with open(file,mode='r') as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if gene_name and gene_seq:
                    gene_dict[gene_name]=gene_seq
                gene_match= re.findall(r'gene:(\S+)',line)
                if gene_match:
                    gene_name = gene_match[0]
                else:
                    gene_name=None
                gene_seq=''
            else:
                if gene_name:
                    gene_seq+=line
    if gene_name and gene_seq:
            gene_dict[gene_name]=gene_seq
    return gene_dict

#CREATE empty new_gene_dict
# FOR each gene_name and gene_seq in genes_dict:
#     SET gene_codons = empty string
#     IF gene_seq contains ATG.+?TAA:
#         ADD " TAA " to gene_codons
#     IF gene_seq contains ATG.+?TAG:
#         ADD " TAG " to gene_codons
#     IF gene_seq contains ATG.+?TGA:
#         ADD " TGA " to gene_codons
#     SET new_gene_dict[gene_name] = gene_codons

new_gene_dict={}
for gene_name, gene_seq in genes_dict.items():
    gene_codons=''
    if re.search(r'ATG.+?TAA',gene_seq):
        gene_codons+=' TAA '
    if re.search(r'ATG.+?TAG',gene_seq):
        gene_codons+=' TAG '
    if re.search(r'ATG.+?TGA',gene_seq):
        gene_codons+=' TGA '
    new_gene_dict[gene_name]=gene_codons

# FUNCTION find_longest_orf(gene_seq):
#     SET target_stops = ["TAA", "TAG", "TGA"]
#     SET longest_orf = empty string
#     FIND all positions of "ATG" in gene_seq
#     FOR each start position in ATG positions:
#         FOR i from start to end of gene_seq, step=3:
#             codon = gene_seq[i:i+3]
#             IF codon is in target_stops:
#                 current_orf = gene_seq[start : i+3]
#                 IF length of current_orf > length of longest_orf:
#                     longest_orf = current_orf
#                 BREAK the loop
#     RETURN longest_orf

def find_longest_orf(gene_seq):
    target_stops = ['TAA', 'TAG', 'TGA']  
    longest_orf = '' 

    ATG_positions = [m.start() for m in re.finditer('ATG', gene_seq)]
    for start in ATG_positions:
        for i in range(start, len(gene_seq) - 2, 3):
            codon = gene_seq[i:i+3] 
            if codon in target_stops:
                orf = gene_seq[start:i+3]
                if len(orf) > len(longest_orf):
                    longest_orf = orf
                break  

    return longest_orf

#     CALL read_fasta to get genes_dict
#     BUILD new_gene_dict with stop codons
#     CREATE empty gene_longest_orf_dict
#     FOR each gene_name and gene_seq in genes_dict:
#         longest_orf = find_longest_orf(gene_seq)
#         gene_longest_orf_dict[gene_name] = longest_orf
#     OPEN "stop_genes.fa" in write mode
#     FOR each gene_name in genes_dict:
#         orf_seq = gene_longest_orf_dict[gene_name]
#         stop_codon = new_gene_dict[gene_name]
#         WRITE header: >gene_name stops=stop_codon
#         WRITE orf_seq
#     CLOSE file

if __name__ == "__main__":
    genes_dict = read_fasta('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')

    gene_longest_orf_dict = {}
    for gene_name, gene_seq in genes_dict.items():
        longest_orf = find_longest_orf(gene_seq)
        gene_longest_orf_dict[gene_name] = longest_orf
with open("stop_genes.fa", "w") as g:
    for gene_name in genes_dict.keys():
        orf_seq = gene_longest_orf_dict.get(gene_name, "")
        stop_codon = new_gene_dict.get(gene_name, "")
        header = f">{gene_name} stops={stop_codon}"
        
        g.write(header + "\n")
        g.write(orf_seq + "\n")

