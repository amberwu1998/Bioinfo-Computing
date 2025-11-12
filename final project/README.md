# MS/MS Viewer

A Python program for visualizing and analyzing peptide fragmentation spectra from mass spectrometry data. This tool reads mzXML files, calculates theoretical peptide b-ion and y-ion masses, matches them against experimental peaks, and generates annotated spectra to help determine whether a peptide is a good match to the observed spectrum.

## Features

- **mzXML File Parsing**: Efficiently extracts MS/MS spectrum data from mzXML files (including gzip-compressed files)
- **Ion Mass Calculation**: Computes theoretical b-ion and y-ion masses for peptide sequences
- **Peak Matching**: Intelligently matches experimental peaks to theoretical ions with configurable mass tolerance
- **Annotated Visualization**: Generates publication-quality spectra with color-coded ion annotations
- **Input Validation**: Comprehensive error checking for file formats and peptide sequences
- **Intensity Filtering**: Reduces noise by filtering out low-intensity peaks (configurable threshold)

## Installation

### Requirements

- Python 3.6+
- matplotlib
- Standard library modules: xml.etree.ElementTree, base64, array, gzip

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/msms-viewer.git
cd msms-viewer

# Install dependencies
pip install matplotlib
```

No additional dependencies are required beyond matplotlib and Python's standard library.

## Usage

### Basic Usage

```bash
python final_project.py <mzxml_file> <scan_number> <peptide_sequence>
```

### Arguments

- `<mzxml_file>`: Path to an mzXML file (can be gzip-compressed with .gz extension)
- `<scan_number>`: The MS/MS scan number to analyze (integer)
- `<peptide_sequence>`: The peptide sequence to search for (amino acids will be converted to uppercase)

### Example

```bash
python final_project.py sample_data.mzXML 1234 PEPTIDEK
```

This will:
1. Extract the spectrum from scan 1234 in the mzXML file
2. Calculate b-ions and y-ions for the peptide sequence PEPTIDEK
3. Match experimental peaks to theoretical ions
4. Display an annotated spectrum plot

## Output

The program generates an interactive matplotlib figure showing:

- **Gray peaks**: All experimental peaks detected in the spectrum
- **Blue peaks with labels**: Matched b-ions (e.g., b1, b2, b3, ...)
- **Red peaks with labels**: Matched y-ions (e.g., y1, y2, y3, ...)
- **X-axis**: m/z values (mass-to-charge ratio)
- **Y-axis**: Peak intensities

A high proportion of blue and red annotations relative to gray peaks indicates a good match between the peptide and spectrum.

## Technical Details

### Supported Amino Acids

The program supports all 20 standard amino acids:
A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y

### Ion Calculations

- **B-ions**: Start from the N-terminus with an initial mass of 1 Da
- **Y-ions**: Start from the C-terminus with an initial mass of 19 Da
- Mass values for each amino acid are based on monoisotopic masses

### Peak Matching Algorithm

The peak matching uses the following strategy:

1. Calculate all theoretical b-ion and y-ion m/z values
2. For each theoretical ion, search for experimental peaks within a mass tolerance window (default: 0.5 m/z)
3. Select the highest-intensity peak within the window as the match
4. Filter out peaks with intensity < 5% of the maximum intensity to reduce noise
5. Prevent double-matching by tracking which experimental peaks have already been assigned

This approach prioritizes signal reliability while minimizing false positives.

### File Format

The program expects valid mzXML files containing MS/MS spectra. The mzXML format stores mass spectrometry data in XML with base64-encoded peak data. The parser automatically handles:

- Namespace detection for compatibility with different mzXML sources
- Base64 decoding of peak data
- Platform-specific byte order detection and correction
- Both regular and gzip-compressed files

## Error Handling

The program provides informative error messages for common issues:

- **File not found**: If the mzXML file doesn't exist
- **Scan not found**: If the specified scan number is not present in the file
- **Invalid amino acid**: If the peptide sequence contains non-standard amino acids
- **Invalid input**: If the number of command-line arguments is incorrect

## Project Architecture

### File Structure

```
msms-viewer/
├── final_project.py          # Main entry point
├── msms_viewer_class.py      # MSMSViewer class with core functionality
└── README.md                 # This file
```

### Design Decisions

**Modular Design**: The code separates concerns into a reusable MSMSViewer class and a simple script interface, making it easy to integrate the viewer into other applications.

**Peak Matching Strategy**: The "highest intensity" approach within tolerance windows is used because more intense peaks are typically more reliable in mass spectrometry, reducing false positives.

**Simplified Ion Model**: The program uses a basic +1 and +19 model for b-ion and y-ion masses respectively, without accounting for neutral losses (water, ammonia). This provides clear, interpretable results suitable for basic analysis.

**Visualization Approach**: Stem plots were chosen over alternative plot types because they clearly show peak heights and positions, which is crucial for spectral interpretation.

## Scientific Background

### Mass Spectrometry Proteomics

Tandem mass spectrometry (MS/MS) is a key technique in proteomics for identifying proteins in complex samples. When a peptide ion is fragmented in the mass spectrometer, it breaks at peptide bonds, producing two ion series:

- **B-ions**: Fragments containing the N-terminus
- **Y-ions**: Fragments containing the C-terminus

By analyzing the pattern of observed ions, researchers can determine the peptide's amino acid sequence, which enables protein identification.

## Dependencies

- **matplotlib**: For visualization (pip-installable)
- **xml.etree.ElementTree**: Standard library XML parser
- **base64**: Standard library binary data encoding/decoding
- **array**: Standard library efficient array operations
- **gzip**: Standard library compression support

## References

- Steen, H., & Mann, M. (2004). The ABC's (and XYZ's) of peptide sequencing. *Nature Reviews Molecular Cell Biology*, 5(9), 699-711.
- mzXML format: https://sashimi.sourceforge.net/schema_revision/mzXML_3.2.pdf
