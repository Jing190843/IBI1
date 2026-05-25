import re

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

def find_longest_orf(seq, stop):
    pattern = re.compile(r'ATG(?:...)*?' + stop)
    candidates = pattern.findall(seq)
    valid = [s for s in candidates if len(s) % 3 == 0]
    if not valid:
        return ""
    return max(valid, key=len)

def split_codons(seq):
    return [seq[i:i+3] for i in range(0, len(seq), 3)]

def count_codon_ratio(codon_list):
    total = len(codon_list)
    count = {}
    for codon in codon_list:
        count[codon] = count.get(codon, 0) + 1
    ratio = {cod: round(num/total, 4) for cod, num in count.items()}
    return count, ratio, total

if __name__ == "__main__":
    genes_dict = read_fasta('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
    input_stop = input("Enter stop codon (TAA, TAG, TGA): ").strip().upper()
    
    if input_stop not in ['TAA', 'TAG', 'TGA']:
        print("Invalid codon")
    else:
        for gene_name, gene_seq in genes_dict.items():
            print("\n=====================")
            print("Gene:", gene_name)
            
            longest_seq = find_longest_orf(gene_seq, input_stop)
            
            if not longest_seq:
                print("No valid ORF")
                continue
            
            print("Longest ORF:", longest_seq)
            print("Length:", len(longest_seq))
            
            codons = split_codons(longest_seq)
            print("Codons:", codons)
            
            count, ratio, total = count_codon_ratio(codons)
            for codon, num in count.items():
                print(f"{codon}: {num} times, {ratio[codon]*100:.2f}%")