'''
Write a program to count the number of spectra in the file
"Data1.mzXML.gz" using ElementTree’s iterparse function.

1)How many MS (attribute "msLevel" is 1) spectra
(tag "scan")
are there?

2) How many MS/MS (attribute "msLevel" is 2) spectra
(tag "scan")
are there?

3) How many MS/MS spectra have precursor m/z value
between 750 and 1000 Da? 
'''

import gzip
import xml.etree.ElementTree as ET

document = "Data1.mzXML.gz"
ns = "{http://sashimi.sourceforge.net/schema_revision/mzXML_2.0}"

ms_level_1 = 0
ms_level_2 = 0
precursor_count = 0

with gzip.open(document, mode='rt') as f:
    
    for event,ele in ET.iterparse(f):

        if ele.tag == (ns+'scan'):
            ms_level = int(ele.attrib.get('msLevel', 0))
            
            if ms_level == 1:
                ms_level_1 += 1
            if ms_level == 2:
                ms_level_2 += 1

        if ele.tag == (ns+'precursorMz'):
            if float(ele.text)>=750 and float(ele.text)<=1000:
               precursor_count += 1
            
        ele.clear()

print('number of msLevel1:', ms_level_1)
print('number of msLevel2:', ms_level_2)
print('precursor count:', precursor_count)
                
                


