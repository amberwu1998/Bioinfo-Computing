'''
Class Project: MS/MS Viewer
Write a program to display peptide fragmentation spectra from an mzXML file. 
- The program will take an mzXML file, a scan number, and a peptide sequence
as input.
- The peptide's b-ion and y-ion m/z values should be computed, and peaks
matching these m/z values annotated with appropriate labels. 
- The output figure/plot should aid the user in determining whether or not
the peptide is a good match to the spectrum.
'''

import sys
from msms_viewer_class import MSMSViewer

if len(sys.argv) != 4:
    print("Please correct your input")
    sys.exit(1)

# Get input parameters
xml_file = sys.argv[1]
scan_number = int(sys.argv[2])
peptide = sys.argv[3].upper()

# Create viewer instance and process spectrum
viewer = MSMSViewer()

# Extract spectrum
spectrum = viewer.extract_spectrum(xml_file, scan_number)
if not spectrum:
    print("Could not find scan number")
    sys.exit(1)

mzs, ints = spectrum

# Calculate theoretical ions
b_ions, y_ions = viewer.calculate_theoretical_ions(peptide)

if not b_ions and not y_ions:
    print("No valid ions could be calculated. Check peptide sequence.")
    sys.exit(1)

# Match peaks
matches = viewer.match_peaks(mzs, ints, b_ions, y_ions)

# Create and show plot
plt = viewer.plot_spectrum(mzs, ints, matches, peptide, scan_number)
plt.show()



