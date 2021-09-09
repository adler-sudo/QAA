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
parser.add_argument("-n1", help="number of reads in input file 1")
parser.add_argument("-i2", help="input trimmed gzipped fastq read 2")
parser.add_argument("-n2", help="number of reads in input file 2")
parser.add_argument("-o", help="output histogram file name")
parser.add_argument("-t", help="histogram title")
args = parser.parse_args()

# define globals
input_file_read_1: str = args.i1
num_reads_1: int = int(args.n1)
input_file_read_2: str = args.i2
num_reads_2: int = int(args.n2)
output_file: str = args.o
histogram_title: str = args.t

# define postion qscore average function
def seq_lengths(file: str, num_reads: int):
    """
    Given trimmed gzipped fastq, return array containing all lengths
    
    Paramteters:
    ------------
    file : str
        trimmed gzip fastq file

    Returns:
    --------
    mean : numpy array
        array of read lengths
    """

    recordcount: int = 0
    read_lengths_array = np.zeros([num_reads, 1]) 

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
        read_lengths_array[recordcount - 1, 0] = read_length

    f.close()

    return read_lengths_array

# generate trimmed read lengths for each file
trimmed_lengths_read_1 = seq_lengths(file=input_file_read_1,num_reads=num_reads_1)
trimmed_lengths_read_2 = seq_lengths(file=input_file_read_2,num_reads=num_reads_2)

# generate and plot dual histogram
bins = len(np.unique(trimmed_lengths_read_1))

plt.hist([trimmed_lengths_read_1.flatten(), trimmed_lengths_read_2.flatten()],bins=bins,label=['Read 1','Read 2'])
plt.yscale('log')
plt.title(histogram_title)
plt.xlabel('Length')
plt.ylabel('Occurrences (log10 scale)')
plt.legend()
plt.savefig(output_file)
