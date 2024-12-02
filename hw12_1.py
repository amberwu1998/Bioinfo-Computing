'''
Write a python program using SQLObject to lookup the scientific name
for a user-supplied organism name.
'''

from model1 import *
import sys

query = str(sys.argv[1])

try:
    hsname = Name.selectBy(name=query)[0]
except IndexError:
    print("Can't find name "+query)
    sys.exit(1)

#print(Name.selectBy(name=query))
print(hsname.taxa.scientificName)




