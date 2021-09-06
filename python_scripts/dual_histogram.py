#!/usr/bin/env python

# import modules
import argparse
import os
import gzip
import matplotlib.pyplot as plt
import numpy as np


# define arparser
parser = argparse.ArgumentParser(description="develop historgram of means for each position of a series of reads")
parser.add_argument("-i1", help="input trimmed gzipped fastq read 1")
parser.add_argument("-i2", help="input trimmed gzipped fastq read 2")
parser.add_argument("-o", help="output histogram file name")
parser.add_argument("-t", help="histogram title")
args = parser.parse_args()

# define globals
input_file_read_1: str = args.i1
input_file_read_2: str = args.i2
output_file: str = args.o
histogram_title: str = args.t

# define postion qscore average function
def seq_lengths(file: str):
    """
    Given trimmed gzipped fastq, return array containing all lengths
    
    Paramteters:
    ------------
    file : str
        trimmed gzip fastq file

    Returns:
    --------
    mean : list
        list of read lengths
    """

    recordcount: int = 0
    read_lengths_list: list = []

    f = gzip.open(file, 'rt')

    while True:
        
        # read in next record
        record: list = [f.readline() for _ in range(4)]
        
        # break if empty (end of file)
        if record[0] == '':
            break
        
        recordcount += 1

        # update statement
        if recordcount % 500000 == 0:
            print(recordcount)
        
        # grab length of read and append to list
        read_length: int = len(record[1])
        read_lengths_list.append(read_length)

    f.close()

    return read_lengths_list

# generate trimmed read lengths for each file
trimmed_lengths_read_1: list = seq_lengths(file=input_file_read_1)
trimmed_lengths_read_2: list = seq_lengths(file=input_file_read_2)

# generate and plot dual histogram
shortest_length = min(trimmed_lengths_read_1 + trimmed_lengths_read_2)
longest_length = max(trimmed_lengths_read_1 + trimmed_lengths_read_2)

bins = np.linspace(
    shortest_length,
    longest_length,
    10
)

plt.hist(trimmed_lengths_read_1,bins=bins,label='Read 1',alpha=0.5)
plt.hist(trimmed_lengths_read_2,bins=bins,label='Read 2',alpha=0.5)
plt.yscale('log')
plt.title(histogram_title)
plt.xlabel('Length')
plt.ylabel('Occurrences')
plt.legend()
plt.savefig(output_file)
