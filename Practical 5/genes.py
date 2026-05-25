# Import required libraries for plotting and calculations
import matplotlib.pyplot as plt
import numpy as np

# Create a dictionary to store gene names and their expression levels
genes_dic = {'TP53': 12.4, 'EGFR': 15.1, 'BRCA1': 8.2, 'PTEN': 5.3, 'ESR1': 10.7}

# Add a new gene (MYC) and its expression value to the dictionary
genes_dic['MYC'] = 11.6

# Convert dictionary keys (gene names) and values (expression levels) into lists
genes = list(genes_dic.keys())
values = list(genes_dic.values())

# Calculate and print the average gene expression level
print("Average gene expression level:", np.mean(values))

# ================ Validation Variable & Input Check =================
# Create a variable to store user input and check if the gene is valid
# This variable confirms whether the input gene is legal/exists
user_input_gene = input("\nEnter a gene name to check validity (e.g., TP53, MYC): ").strip().upper()

# Check if the input gene exists in the dictionary (validation logic)
if user_input_gene in genes_dic:
    print(f" VALID GENE: {user_input_gene}")
    print(f"Expression level of {user_input_gene} = {genes_dic[user_input_gene]}")
else:
    print(f" INVALID GENE: {user_input_gene} is not in the gene list.")

# ================= Plotting Gene Expression Levels =================
plt.bar(genes, values)

# Set chart labels and title (English)
plt.xlabel('Genes')
plt.ylabel('Expression Levels')
plt.title('Gene Expression Levels')

# Set Y-axis limit for better visualization
plt.ylim(0, max(values) * 1.1)

# Adjust layout to prevent label overlapping
plt.tight_layout()

# Show the plot
plt.show()