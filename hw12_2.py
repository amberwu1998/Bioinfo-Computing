'''
Write a python program using SQLObject to find the taxonomic lineage of
a user-supplied organism name.
-- Make sure you use the small_taxa.db3 file from the course data-folder

'''

import sys
from model2 import *
init()


organism_name = " ".join(sys.argv[1:])
    
try:
    results = Name.select(Name.q.name == organism_name)
except SQLObjectNotFound:
    print("Error accessing database", file=sys.stderr)
    sys.exit(1)
    
if results.count() == 0:
    print("No organism found with this name", file=sys.stderr)
    sys.exit(1)

try:
    name_record = results[0]
    taxonomy = name_record.taxonomy
except IndexError:
    print("Error accessing taxonomy data", file=sys.stderr)
    sys.exit(1)
    
print("Organism",taxonomy.scientific_name,"has rank",taxonomy.rank)

print("Taxonomic lineage:")

lineage = []
current = taxonomy
while current != current.parent:
    lineage.append(current.rank + ": " + current.scientific_name)
    current = current.parent
lineage.append(current.rank + ": " + current.scientific_name)

for level in reversed(lineage):
    print(level)











