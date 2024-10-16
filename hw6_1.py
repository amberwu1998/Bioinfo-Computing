'''
Write a program that reads the microarray data in “data.csv” and
computes the mean and standard deviation of the expression values of
a specific gene overall, and within each sample category.
- Get the name of the microarray datafile from the command-line.
- Get the name of the gene from the command-line.
'''

import sys
import csv
import math

if len(sys.argv) < 3:
    print('Wrong number of input.', file=sys.stderr)
    sys.exit(1)

import_file = sys.argv[1]
gene = sys.argv[2]
f = open(import_file)


rows = csv.DictReader(f, dialect='excel')

category_value = {'total':[]}
for r in rows:
    if gene not in r:
        print('No gene found in data.')
    category = r['TUMOUR']
    gene_value = r[gene]
    #print('Category:', category)
    #print('Gene Value:', gene_value)

    if category not in category_value:
        category_value[category]= []
    category_value[category].append(float(gene_value))
    category_value['total'].append(float(gene_value))
#print('Category Value:', category_value)
#sum_value = sum(category_value['total'])
#print('Sum:', sum_value)


for cat in category_value.keys():
    dict_val = category_value[cat]
    mean = sum(dict_val)/len(dict_val)
    stddev = math.sqrt(sum((x-mean)**2 for x in dict_val)/len(dict_val))
    print('Category:', cat, 'Mean:', mean, 'Standard Deviation:', stddev)
    
    
f.close()
