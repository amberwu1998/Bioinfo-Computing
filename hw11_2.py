'''
Write a python program to lookup the scientific name for
a user-supplied organism name.
'''

import sys
import sqlite3

tid = [str(sys.argv[1])]
conn = sqlite3.connect('taxa.db3')
c = conn.cursor()

c.execute('''
   select scientific_name from taxonomy
    where
        tax_id = (
        select tax_id from name
        where name = ? )
''',tid)


for row in c:
    print(' '.join(row))



