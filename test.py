'''
Write a program to pick out, and print,
the references of a XML format UniProt entry, in a nicely formatted way.
'''

import xml.etree.ElementTree as ET
import urllib.request

thefile = urllib.request.urlopen(
    'http://www.uniprot.org/uniprot/Q9H400.xml'
                         )
document = ET.parse(thefile)
root = document.getroot()
ns = '{http://uniprot.org/uniprot}'

entry = root.find(ns+'entry')
#print('Entry:', entry.attrib)

reference = entry.findall(ns+'reference')

for ele in reference:
    number = ele.attrib['key']
    print('\n')
    print("====", 'Reference', number, "====")
    
    
    citation = ele.find(ns+'citation')
    if citation is not None:
        print('-Citation Information-')
        for attrib, value in citation.attrib.items():
            print(attrib + ':' + ' ' + value)
        print('\n')
        
        title = citation.find(ns+'title')
        if title is not None:
            print('-Title-')
            print(title.text)
            print('\n')

        authorlist = citation.find(ns+'authorList')
        authors = []
        if authorlist is not None:
            for ele in authorlist:
                for name,author in ele.attrib.items():
                    authors.append(author)
                    names = ', '.join(authors)
            print('-AuthorList-')
            print(names)
            print('\n')

        dbreference = citation.findall(ns+'dbReference')
        if dbreference:
            print('-Database Reference-')
            for ele in dbreference:
                ref = ''.join(
                    [key+':'+value+' ' for key,value in ele.attrib.items()]
                    )
                print(ref)
        print('\n')

    scope = ele.findall(ns+'scope')
    if scope is not None:
        print('-Scope-')
        for texts in scope:
            print(texts.text)
        print('\n')
