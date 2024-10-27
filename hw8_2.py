'''
Write a pandas-based program to:
1) determine the number of genes with at least two distinct peptides
in all samples.
2) determine the number of genes with at least two distinct peptides
in at least one sample.
Hint: Slide 21 contains the essential tricks
'''

import numpy as np
import pandas as pd

df = pd.read_csv("proteomics.summary.tsv",sep='\t')
#df.info()
#print("Data from Input File",df,sep='\n',end='\n\n')


df2 = df.min()>=2
all_samples = df2.sum()
#print('df2:', df2)
print('all samples with at least two distinct peptides:', all_samples)

df3 = df.max()>=2
at_least_one_sample = df3.sum()
#print('df3:', df3)
print('at least one sample with at least two distinct peptides:', at_least_one_sample)





