import re

def read_fasta(file_path):
    """
    Read a FASTA file and return a dictionary: {gene_name: full_sequence}
    Handles multi-line sequences correctly.
    """
    gene_dict = {}
    current_gene = None
    current_seq = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Header line: extract gene name
            if line.startswith(">"):
                # Save previous gene if exists
                if current_gene is not None:
                    gene_dict[current_gene] = ''.join(current_seq)

                # Match gene name pattern: gene:xxxx
                gene_match = re.search(r'gene:(\S+)', line)
                if gene_match:
                    current_gene = gene_match.group(1)
                else:
                    current_gene = None  # skip invalid header
                current_seq = []

            # Sequence line
            else:
                if current_gene is not None:
                    current_seq.append(line)

        # Save the last gene
        if current_gene is not None:
            gene_dict[current_gene] = ''.join(current_seq)

    return gene_dict


def find_longest_orf(sequence):
    """
    Find the longest ORF starting with ATG and ending with in-frame stop codon (TAA/TAG/TGA)
    Returns the longest ORF DNA sequence.
    """
    stop_codons = {'TAA', 'TAG', 'TGA'}
    longest_orf = ''

    # Find all start codon positions
    start_positions = [m.start() for m in re.finditer(r'ATG', sequence)]

    for start in start_positions:
        # Read codons in triplets (in-frame)
        for i in range(start, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
            if codon in stop_codons:
                current_orf = sequence[start:i+3]
                if len(current_orf) > len(longest_orf):
                    longest_orf = current_orf
                break  # stop at first in-frame stop codon

    return longest_orf


def get_stop_codons_in_orf(orf_seq):
    """
    Detect which stop codons are present in the ORF.
    Return a string like 'TAA TAG'
    """
    stops_found = []
    if 'TAA' in orf_seq:
        stops_found.append('TAA')
    if 'TAG' in orf_seq:
        stops_found.append('TAG')
    if 'TGA' in orf_seq:
        stops_found.append('TGA')
    return ' '.join(stops_found)


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    # Read input FASTA file
    input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    genes = read_fasta(input_file)

    # Open output file
    with open("stop_genes.fa", "w") as out_f:
        for gene_name, seq in genes.items():
            # Get longest ORF
            orf = find_longest_orf(seq)

            # Skip genes with NO stop codon
            if not orf:
                continue

            # Get stop codons
            stops = get_stop_codons_in_orf(orf)
            if not stops:
                continue

            # Write to output FASTA
            out_f.write(f">{gene_name} stops={stops}\n")
            out_f.write(orf + "\n")

    print("Task completed! Results saved to stop_genes.fa")
