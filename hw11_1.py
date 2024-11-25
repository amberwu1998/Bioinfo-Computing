'''
Find potential fruit fly / yeast orthologs
-- Download FASTA files drosoph-ribosome.fasta.gz and yeast-ribosome.fasta.gz
    from the course data-directory.
-- Uncompress and format each FASTA file for BLAST
-- Search fruit fly ribosomal proteins against yeast ribosomal proteins

For each fruit fly query, output the best yeast protein if it has a
significant E-value.
-- What ribosomal protein is most highly conserved between
fruit fly and yeast?
'''

# Special modules for running blast
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIXML

blast_prog   = '/usr/local/bin/blastp'
blast_query = 'blastdb/drosoph-ribosome.fasta'
blast_db    = 'blastdb/yeast-ribosome.fasta'


cmdline = NcbiblastpCommandline(cmd=blast_prog,
                                query=blast_query,
                                db=blast_db,
                                outfmt=5,
                                out="blast_results.xml")

stdout, stderr = cmdline()


result_handle = open("blast_results.xml")


most_conserved = None 
lowest_e = None

for blast_result in NCBIXML.parse(result_handle):
    query_id = blast_result.query
    best_e = None
    best_title = None

    
    for alignment in blast_result.alignments:
        #print("Alignment:", alignment)
        for hsp in alignment.hsps:
            #print('Hsps:', hsp)
            
            if hsp.expect < 1e-5:
                if best_e is None or hsp.expect < best_e:
                    best_e = hsp.expect
                    best_title = alignment.title
                    #print(best_e)
                    

    if best_title:
        if lowest_e is None or best_e < lowest_e:
            lowest_e = best_e
            most_conserved = {
                "query": query_id,
                "subject": best_title,
                "evalue": best_e,
            }
            
        print('****Best Alignment****')
        print('query:', blast_result.query)
        print('subject:', alignment.title)
        print('length:', alignment.length)
        print('e value:', best_e)
        print(hsp.query[0:75] + '...')
        print(hsp.match[0:75] + '...')
        print(hsp.sbjct[0:75] + '...')

    else:
        print('****No Alignment****')
        print('query:', blast_result.query)
        print('subject:', alignment.title)
        print('"No significant alignments found')

if most_conserved:
    print('****Most conserved Protein****')
    print('query:', most_conserved["query"])
    print('subject:', most_conserved["subject"])
    print('e value:', most_conserved["evalue"])

else:
    print('No Highly Conserved Protein Found')
    
result_handle.close()





