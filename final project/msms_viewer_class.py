# Import modules
import xml.etree.ElementTree as ET  
import sys  
from base64 import b64decode  
from array import array  
import matplotlib.pyplot as plt  
import gzip 


class MSMSViewer:
    def __init__(self):
        # Dictionary of amino acid masses
        self.aa_masses = {
            'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
            'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
            'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
            'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06
        }

    def validate_sequence(self, peptide):
        #Checks if peptide sequence contains only valid amino acids
        valid_aa = self.aa_masses.keys()
        for aa in peptide:
            if aa not in valid_aa:
                print('Invalid amino acid in sequence', file=sys.stderr)
                return False
        return True

    def extract_spectrum(self, xml_file, scan_number):
        #Extracts MS/MS spectrum data from mzXML file
        ns = None
        target_scan = None
        
        try:
            if xml_file.endswith('.gz'):
                xmldoc = gzip.open(xml_file)
            else:
                xmldoc = open(xml_file)

        except FileNotFoundError:
            print('File ',xml_file,' was not found', file=sys.stderr)

        for event, ele in ET.iterparse(xmldoc):
            if not ns:
                p = ele.tag.find('}')
                if p >= 0:
                     ns = ele.tag[:(p+1)]

            # Scan element processing
            if event == 'end' and ele.tag == ns+'scan':
                if int(ele.attrib['num']) == scan_number:
                    if int(ele.attrib['msLevel']) == 2:
                        peaks_element = ele.find(ns+'peaks')
                        if peaks_element is not None:
                            peaks = array('f', b64decode(peaks_element.text))
                            if sys.byteorder != 'big':
                                peaks.byteswap()
                            mzs = peaks[::2]
                            ints = peaks[1::2]
                            target_scan = (mzs, ints)
                ele.clear()
            
        xmldoc.close()
        return target_scan


    def calculate_theoretical_ions(self, peptide):
        #Calculate theoretical b and y ion mass
        n = len(peptide)
        b_ions = []
        y_ions = []

        # Calculate b-ions
        mass_n = 1
        for i in range(n):
            mass_n += self.aa_masses[peptide[i]]  
            b_ions.append((mass_n, 'b' + str(i+1))) 

        # Calculate y-ions
        mass_c = 19
        for i in range(n-1,-1,-1): 
            mass_c += self.aa_masses[peptide[i]]
            y_ions.append((mass_c, 'y' + str(n-i))) 

        return b_ions, y_ions


    def match_peaks(self, mzs, ints, b_ions, y_ions, tolerance=0.5):
        #Match experimental peaks to theoretical ions

        matches = []          
        used_peaks = set()   # prevent double-matching

        intensity_threshold = max(ints) * 0.05
        
        all_ions = b_ions + y_ions
        #print('All_ions', all_ions)
        
        # For each theoretical ion mass and label
        for theo_mz, ion_label in all_ions:
            best_match = None   
            best_intensity = 0 
        
            for i in range(len(mzs)):
                exp_mz = mzs[i]
                intensity = ints[i]
                if i in used_peaks or intensity < intensity_threshold:
                    continue
                
                # Check if experimental peak is within tolerance window
                if abs(exp_mz - theo_mz) <= tolerance:
                    if intensity > best_intensity:
                        best_match = (i, exp_mz, intensity)
                        best_intensity = intensity
            

            # If found a match, add it to results
            if best_match:
                idx, exp_mz, intensity = best_match
                matches.append((exp_mz, intensity, ion_label))
                used_peaks.add(idx)  
        
        return matches


    def plot_matches(self, mzs_matched, intensities_matched, ion_matches, color):
        if ion_matches:  # Only plot if there are matches
            plt.stem(mzs_matched, intensities_matched, linefmt=color, markerfmt='')
            for mz, intensity, label in ion_matches:
                plt.text(mz, intensity, label, color=color, fontsize=8)

    def plot_spectrum(self, mzs, ints, matches, peptide, scan_number):
        plt.figure(figsize=(12, 6))
        
        # Plot all peaks in gray
        plt.stem(mzs, ints, linefmt='gray', markerfmt='')
        
        # Separate b and y ions
        b_matches = [(mz, intensity, label) for mz, intensity, label in matches if label.startswith('b')]
        y_matches = [(mz, intensity, label) for mz, intensity, label in matches if label.startswith('y')]
        
        # Extract m/z and intensities for b-ions
        if b_matches:
            b_mzs = [ion[0] for ion in b_matches]
            b_intensities = [ion[1] for ion in b_matches]
            self.plot_matches(b_mzs, b_intensities, b_matches, 'blue')
        
        # Extract m/z and intensities for y-ions
        if y_matches:
            y_mzs = [ion[0] for ion in y_matches]
            y_intensities = [ion[1] for ion in y_matches]
            self.plot_matches(y_mzs, y_intensities, y_matches, 'red')
        
        plt.xlabel('m/z')
        plt.ylabel('Intensity')
        plt.title('MS/MS Spectrum')
        
        return plt








