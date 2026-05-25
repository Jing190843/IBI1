# Define a function to calculate the mass of a protein sequence
def protein_mass(sequence):
    sequence = sequence.upper()
    mass_table = {
        'G': 57.02,
        'A': 71.04,
        'S': 87.03,
        'P': 97.05,
        'V': 99.07,
        'T': 101.05,
        'C': 103.01,
        'I': 113.08,
        'L': 113.08,
        'N': 114.04,
        'D': 115.03,
        'Q': 128.06,
        'K': 128.09,
        'E': 129.04,
        'M': 131.04,
        'H': 137.06,
        'F': 147.07,
        'R': 156.10,
        'Y': 163.06,
        'W': 186.08
    }
    
    total_mass = 0.0
    invalid_found = False

    # Calculate the total mass of the protein sequence, and warn if any invalid amino acids are found
    for amino_acid in sequence:
        if amino_acid in mass_table:
            total_mass += mass_table[amino_acid]
        else:
            print(f"Warning: '{amino_acid}' is not a valid amino acid.")
            invalid_found = True

    if invalid_found:
        print("Warning: Sequence contains invalid amino acids — mass may be incorrect.\n")
    else:
        print(f"The total mass of the sequence 'AAAAAA' is: {total_mass:.2f} amu\n")
    
    return total_mass

# : User input function 
def input_protein_sequence():
    print("===== Protein Mass Calculator =====")
    print("Enter 'quit' to exit.\n")
    
    while True:
        user_seq = input("Enter protein sequence: ").strip()
        
        # Exit if user types quit
        if user_seq.lower() == "quit":
            print("Exiting program...")
            break
        
        # Skip empty input
        if not user_seq:
            print("Error: Empty sequence! Please try again.\n")
            continue
        
        # Calculate and show result
        protein_mass(user_seq)

# Main program
if __name__ == "__main__":

    #Example usage
    protein_mass("AAAAAA")

    # Input sequence
    input_protein_sequence()