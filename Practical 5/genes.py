import matplotlib.pyplot as plt
import numpy as np
genes_dic={'TP53':12.4,'EGFR':15.1,'BRCA1':8.2,'PTEN':5.3,'ESR1':10.7}
genes_dic['MYC']=11.6
genes=list(genes_dic.keys())
values=list(genes_dic.values())
print("average gene expression level:", np.mean(values))
plt.bar(genes,values)
plt.xlabel('Genes')     
plt.ylabel('Expression Levels')
plt.title('Gene Expression Levels')
plt.ylim(0,max(values)*1.1)
plt.tight_layout()
plt.show()
