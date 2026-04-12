import re
import matplotlib.pyplot as plt

# FUNCTION read_fasta(file):
#     CREATE empty dictionary gene_dict
#     SET gene_name = None
#     SET gene_seq = empty string
#     OPEN the input file in read mode
#     FOR each line in the file:
#         REMOVE whitespace from the line
#         IF line is empty:
#             SKIP the line
#         IF line starts with '>':
#             IF gene_name exists AND gene_seq is not empty:
#                 STORE gene_seq into gene_dict with gene_name as key
#             EXTRACT gene name from line using regex pattern 'gene:(\S+)'
#             IF gene name is found:
#                 SET gene_name = extracted gene name
#             ELSE:
#                 SET gene_name = None
#             RESET gene_seq to empty string
#         ELSE:
#             IF gene_name is not None:
#                 APPEND current line to gene_seq
#     AFTER processing all lines:
#         IF gene_name exists AND gene_seq is not empty:
#             STORE the last gene into gene_dict
#     RETURN gene_dict

def read_fasta(file):
    gene_dict = {}
    gene_name = None
    gene_seq = ''
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if gene_name and gene_seq:
                    gene_dict[gene_name] = gene_seq
                gene_match = re.findall(r'gene:(\S+)', line)
                if gene_match:
                    gene_name = gene_match[0]
                else:
                    gene_name = None
                gene_seq = ''
            else:
                if gene_name:
                    gene_seq += line
    if gene_name and gene_seq:
        gene_dict[gene_name] = gene_seq
    return gene_dict

# FUNCTION find_longest_orf(seq, stop):
#     CREATE regex pattern: ATG followed by any codons until the given stop codon
#     FIND all matching sequences in the input DNA sequence
#     FILTER valid sequences: only keep sequences with length divisible by 3
#     IF no valid sequences exist:
#         RETURN empty string
#     ELSE:
#         RETURN the longest valid sequence

def find_longest_orf(seq, stop):
    pattern = re.compile(r'ATG(?:...)*?' + stop)
    candidates = pattern.findall(seq)
    valid = [s for s in candidates if len(s) % 3 == 0]
    if not valid:
        return ""
    return max(valid, key=len)

# FUNCTION split_codons(seq):
#     SPLIT DNA sequence into groups of 3 characters (codons)
#     RETURN list of codons

def split_codons(seq):
    return [seq[i:i+3] for i in range(0, len(seq), 3)]

# MAIN PROGRAM:
#     CALL read_fasta to load all gene sequences into genes_dict
#     ASK user to input a stop codon (TAA/TAG/TGA)
#     CONVERT input to uppercase
#
#     IF input is not one of TAA, TAG, TGA:
#         PRINT "Invalid codon"
#     ELSE:
#         CREATE empty list all_codons
#
#         FOR each gene in genes_dict:
#             GET the longest ORF ending with the input stop codon
#             IF longest ORF exists:
#                 SPLIT ORF into codons
#                 ADD all codons to all_codons list
#
#         COUNT total number of codons
#         COUNT frequency of each codon
#         SORT codons by frequency from high to low
#
#         SET font for plotting
#         CREATE a pie chart
#         PLOT codon distribution with labels and percentages
#         SET chart title with the stop codon
#         SAVE chart as image file
#         CLOSE plot
#
#         PRINT "Pie chart saved as codon_pie.png"

if __name__ == "__main__":
    genes_dict = read_fasta('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
    input_stop = input("Enter stop codon (TAA, TAG, TGA): ").strip().upper()

    if input_stop not in ['TAA', 'TAG', 'TGA']:
        print("Invalid codon")
    else:
        all_codons = []
        for gene_name, gene_seq in genes_dict.items():
            longest_seq = find_longest_orf(gene_seq, input_stop)
            if longest_seq:
                codons = split_codons(longest_seq)
                all_codons.extend(codons)

        total = len(all_codons)
        count = {}
        for c in all_codons:
            count[c] = count.get(c, 0) + 1

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        top_codons = [item[0] for item in sorted_items[:64]]
        top_counts = [item[1] for item in sorted_items[:64]]

        plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
        plt.figure(figsize=(70, 70))
        plt.pie(top_counts, labels=top_codons, autopct='%1.1f%%', startangle=90)
        plt.title(f'Codon Distribution (Stop: {input_stop})')
        plt.savefig('codon_pie.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("Pie chart saved as codon_pie.png")