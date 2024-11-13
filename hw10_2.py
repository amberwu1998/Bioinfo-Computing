from Bio import Entrez, SeqIO
import os.path
from Bio.Blast import NCBIWWW,NCBIXML

# Task 1
'''
Write a program using NCBI's E-Utilities to retrieve the ids of RefSeq
human LIME1 proteins from NCBI. 
-- Use the query:
    Homo sapiens[Organism] AND LIME1[Gene Name] AND REFSEQ
-- You do not need the protein sequence!
'''

Entrez.email = 'tw776@georgetown.edu'
query = 'Homo sapiens[Organism] AND LIME1[Gene Name] AND REFSEQ'

handle = Entrez.esearch(db="protein", term=query,
                        usehistory="y")
result = Entrez.read(handle)
handle.close()

count          = int(result["Count"])
session_cookie = result["WebEnv"]
query_key      = result["QueryKey"]
result_ids     = result['IdList']


print('IDs of RefSeq human LIME1 proteins:', result_ids)
#print("Count:",count)
#print("Session_cookie:",session_cookie)
#print("Query Key:",query_key)


handle = Entrez.efetch(db="protein", rettype="gb",
                        webenv=session_cookie, query_key=query_key)
handle.close()



# Task 2
'''
Extend your program to blast the proteins ids vs RefSeq proteins
(refseq_protein) using the NCBI blast web-service:
-- Search all protein ids together (separated by newlines)
-- Use the keyword argument entrez_query to restrict to mouse proteins:
    Mus musculus[Organism]
-- Use the keyword argument expect to restrict to high quality alignments:
    1e-3
'''

query_ids = ','.join(result_ids)
#print(query_ids)
filename = "blastp-refseq_protein_"+query_ids+".xml"
#print(filename)

if not os.path.exists(filename):

    result_handle = NCBIWWW.qblast("blastp", "refseq_protein",
                                   query_ids.replace(',','\n'),
                                   entrez_query="Mus musculus[Organism]",
                                   expect=1e-3)
    blast_results = result_handle.read()
    result_handle.close()

    save_file = open(filename, "w")
    save_file.write(blast_results)
    save_file.close()

blast_output = open(filename).read()
#print('BLAST result:', blast_output)




# Task 3
'''
Further extend your program to filter the results for significance
and display the putative human-mouse orthologs
-- Filter the alignments for E-value at most 1e-5
-- Print only the best hit (smallest E-value) for each query
'''

result_handle = open(filename)
for i, blast_result in enumerate(NCBIXML.parse(result_handle)):
    best_e = 0
    best_title = None
    
    for desc in blast_result.descriptions:
        if desc.e < 1e-5:
            if best_e == 0 or best_e > desc.e:
                best_e = desc.e
                best_title = desc.title
                
    if best_e:
        print('****Best Alignment for '+ result_ids[i] +'****')
        print('Query:', blast_result.query)
        print('Best Sequence:', best_title)
        print('Best E Value:', best_e)

    else:
        print('"No significant alignments found')


result_handle.close()




