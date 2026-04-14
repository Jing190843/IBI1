#define a function to calculate the mass of a protein sequence
def protein_mass(sequence):
    sequence = sequence.upper()
    mass_table ={
        'G': 75.07,
        'A': 71.04,
        'S': 87.03,
        'P': 97.12,
        'V': 99.07,
        'T': 101.11,
        'C': 103.01,
        'I': 113.08,
        'L': 113.08,
        'N': 114.08,
        'D': 115.03,
        'Q': 128.13,
        'K': 128.09,
        'E': 129.04,
        'M': 131.19,
        'H': 137.14,
        'F': 147.18,
        'R': 156.10,
        'Y': 163.18,
        'W': 186.08
    }
    total_mass = 0.0
    # Calculate the total mass of the protein sequence, and warn if any invalid amino acids are found
    for amino_acid in sequence:
        if amino_acid in mass_table:
            total_mass += mass_table[amino_acid]
        else:
            print(f"Warning: '{amino_acid}' is not a valid amino acid.")
    print(f"The total mass of the protein sequence is: {total_mass:.2f} amu")
    return total_mass

#example usage
if __name__ == "__main__":
    protein_mass("AAAAAAA")