#!/usr/local/bin/python

# Script to plot potential regions of autozygosity using data on genotype calls from VCF files
# This is a simple sequential program using the matplotlib module to plot data
# Tom Gaunt, University of Bristol, 2011

# Import relevant python modules: system, plotting, GUI
import sys
import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from Tkinter import *
from tkMessageBox import *
from tkColorChooser import askcolor
from tkFileDialog import askopenfilename

# Function to calculate and return heterozygosity (proportion of variants heterozygous) in a window
def calchet(winhet):
    sum = 0.0
    count = 0.0
    for item in winhet:
        sum += float(item)
        count += 1.0
    return sum / count


# Ask the user for a VCF file (GUI via tkFileDialog) then read through (and ignore) the file header
infilename = askopenfilename(
    defaultextension=".vcf",
    filetypes=[("Variant Call Format", "*.vcf"), ("All files", "*.*")],
)  # sys.argv[1]
infile = open(infilename, "r")
while 1:
    dataline = infile.readline()
    dataline = dataline.strip().split()
    if dataline[0] == "#CHROM":
        break

# Initialise the variables used for plot lists
hzplotx = []
hzploty = []
hetplotx = []
hetploty = []
plotx = []
ploty = []

# Initialise variables reused throughout main program loop
currentchr = "null"
counter = 0
windowhet = []

# Add a new list for each chromosome to the plot variables (these are then lists of lists)
for i in range(25):
    plotx.append([])
    ploty.append([])

# Main program loop - iterates over the rest of the VCF file
while 1:
    # First part of the loop reads in the file, splits out the data into lists
    dataline = infile.readline()
    dataline = dataline.strip().split()
    if len(dataline) < 5:
        break  # We want to finish when we reach the end of the file
    genocodes = dataline[9].split(":")
    chrom = dataline[0]
    if chrom in [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "X",
        "Y",
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
    ]:
        chromn = chrom
    else:
        chromn = chrom[3:]
    if chromn == "X" or chrom == "X":
        chromn = 23
    elif chromn == "Y" or chrom == "Y":
        chromn = 24
    else:
        chromn = int(chromn)
    if chromn != currentchr:
        currentchr = chromn
        windowhet = []
        counter = 0
    pos = dataline[1]
    genotype = genocodes[0]

    # This part determines genotype and sets heterozygosity variable
    if genotype == "0/0" or genotype == "1/1":
        thishet = 0.0
    else:
        thishet = 1.0

    # Add the new value to the window if it is a SNP (denoted by "rs" number)
    if dataline[2][0:2] == "rs":
        windowhet.append(thishet)

    #  Remove the first value from the list if the list is now longer than 20 (the window size), calculate the window heterozygosity and add to plot variable
    if (
        counter > 20 and dataline[2][0:2] == "rs"
    ):  # Note window size is hard coded at 20 here
        null = windowhet.pop(0)
        plotx[chromn].append(pos)
        thisval = float(calchet(windowhet))
        ploty[chromn].append(float(chromn) * 2 + thisval)
    counter += 1

    # Populate the heterozygosity and homozygosity plot variables for each variant
    readdepth = genocodes[1]
    if (
        genotype == "0/0" or genotype == "1/1" or genotype == "0|0" or genotype == "1|1"
    ) and dataline[2][0:2] == "rs":
        hzplotx.append(pos)
        hzploty.append(float(chromn) * 2 + 1 + 0.4)
    elif dataline[2][0:2] == "rs":
        hetplotx.append(pos)
        hetploty.append(float(chromn) * 2 + 1 + 0.6)

# Create the plot figure
fig = plt.figure()
ax = fig.add_subplot(111)

# Create a suitable title from the filename
filelist = infilename.split("/")
filetitle = filelist[-1]
fig.suptitle("File: " + filetitle, fontsize=11)

# Create the plot of variants (homozygous or heterozygous status)
plt.plot(hzplotx, hzploty, "ro", hetplotx, hetploty, "go")

# Add the chromosomes as y-axis ticks
ytick = []
for i in range(1, 25):
    ytick.append(i * 2 + 1)
ax.set_yticks(ytick)
ticklabels = []
for i in range(1, 23):
    ticklabels.append("Chr " + str(i))
ticklabels.append("Chr X")
ticklabels.append("Chr Y")
labels = ax.set_yticklabels(ticklabels)

# Plot the window heterozygosity
for i in range(len(plotx)):
    ax.plot([0, 250000000], [(i + 1) * 2 + 1, (i + 1) * 2 + 1], "k:")
    ax.plot([0, 250000000], [(i + 1) * 2, (i + 1) * 2], "k-")
    ax.plot(plotx[i], ploty[i], "b-")

# Show the plot
plt.show()

# Close the input file
infile.close()
