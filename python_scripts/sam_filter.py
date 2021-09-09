#!/usr/bin/env python

# import necessary modules
import argparse
import os


# define argparser
parser = argparse.ArgumentParser(description="parse contents of SAM file")
parser.add_argument("-f",help="input SAM file")
parser.add_argument("-o",help="output summary file")
args = parser.parse_args()

# define globals
filename: str = args.f
output_summary_file: str = args.o
print("input file:",filename)
print("output summary file:",output_summary_file)

# count reads that properly mapped vs. unmapped 
mapped: int = 0
unmapped: int = 0

# read file
f = open(filename,'r')

while True:

    # read next line
    line: str = f.readline()

    # break if end of file
    if line == '':
        break

    # ignore headers
    if line.startswith("@"):
        continue

    # split components
    line: list = line.split()

    # define each component
    flag = int(line[1])

    # determine if mapped and primary alignment
    if (((flag & 4) != 4) and ((flag & 256) != 256)):
        mapped += 1
    
    # determine if unmapped and primary alignment
    if (((flag & 4) == 4) and ((flag & 256) != 256)):
        unmapped += 1

f.close()

# write to summary file
output_summary_file = open(output_summary_file,'w')
output_summary_file.write('summary of sam file: ' + filename + '\n')
output_summary_file.write('mapped reads: ' + str(mapped) + '\n')
output_summary_file.write('unmapped reads: ' + str(unmapped) + '\n')
output_summary_file.close()

# print the number of mapped and unmapped
print('mapped reads:',mapped)
print('unmapped reads:',unmapped)