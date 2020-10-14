# AutoZplotter

This is a simple Python script to plot autozygosity

*Author: Tom Gaunt*

## Use of the script

This works with Python 2.x (not 3.x or above). The script is executed with ```python autozplotter.py``` on a system that supports Tk GUIs (has been tested on Mac, 
Windows and Linux). 

The software initiates with an "Open file" dialog box that is looking for a single VCF file. When a VCF file is selected the script should produce a matplotlib interactive 
window with representations of homozygosity and heterozygosity. This can be zoomed/panned using standard matplotlib controls.


