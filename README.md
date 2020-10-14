# AutoZplotter

This is a simple legacy Python script to plot autozygosity. The code may well not work on all VCF formats, but is provided in case it is of use to others.

## Use of the script

This works with Python 2.x (not 3.x or above). The script is executed with ```python autozplotter.py``` on a system that supports Tk GUIs (has been tested on Mac, 
Windows and Linux). 

The software initiates with an "Open file" dialog box that is looking for a single VCF file. When a VCF file is selected the script should produce a matplotlib interactive 
window with representations of homozygosity and heterozygosity. This can be zoomed/panned using standard matplotlib controls.

## Citation

If you find this tool of use please cite: Erzurumluoglu et al, "Identifying Highly Penetrant Disease Causal Mutations Using Next Generation Sequencing: Guide to Whole Process." Biomed Research International Volume 2015 |Article ID 923491 | [https://doi.org/10.1155/2015/923491](https://doi.org/10.1155/2015/923491)
