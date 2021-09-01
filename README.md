# RNA-seq Quality Assessment Assignment - Bi 623 (Summer 2021)

Be sure to upload all relevant materials by the deadline and **double check** to be sure that your off-line repository is up-to-date with your on-line repository. Answers to the questions can be submitted as Github markdown or ```pdf```.

## Objectives
The objectives of this assignment are to use existing tools for quality assessment and adaptor trimming, compare the quality assessments to those from your own software, and to demonstrate your ability to summarize other important information about this RNA-Seq data set.

### Data: 
Each of you will be working with 2 of the demultiplexed file pairs. For all steps below, process the two libraries separately. Library assignments are here: ```/projects/bgmp/shared/Bi623/QAA_data_assignments.txt```

The demultiplexed, gzipped .fastq files are here: ```/projects/bgmp/shared/2017_sequencing/demultiplexed/```

## Do not move, copy, or unzip these data!

# Part 1 – Read quality score distributions

1. Using ```FastQC``` via the command line on Talapas, produce plots of quality score distributions for R1 and R2 reads. Also, produce plots of the per-base N content, and comment on whether or not they are consistent with the quality score plots.

2. Run your quality score plotting script from your Demultiplexing assignment from Bi622. Describe how the ```FastQC``` quality score distribution plots compare to your own. If different, propose an explanation. Also, does the runtime differ? If so, why?

3. Comment on the overall data quality of your two libraries.

# Part 2 – Adaptor trimming comparison

4. Create a new conda environment called ```QAA``` and install ```cutadapt``` and ```Trimmomatic```. Google around if you need a refresher on how to create conda environments. Make sure you check your installations with:
    - ```cutadapt --version``` (should be 3.4)
    -  ```trimmomatic -version``` (should be 0.39)

5. Using ```cutadapt```, properly trim adapter sequences from your assigned files. Be sure to read how to use ```cutadapt```. Use default settings. What proportion of reads (both forward and reverse) were trimmed?

    <details>
    <summary>Try to determine what the adapters are on your own. If you cannot (or if you do, and want to confirm), click here to see the actual adapter sequences used.</summary>
  
    R1: ```AGATCGGAAGAGCACACGTCTGAACTCCAGTCA```
    
    R2: ```AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT```
    </details>

    - *Sanity check*: Use your Unix skills to search for the adapter sequences in your datasets and confirm the expected sequence orientations. Report the commands you used, the reasoning behind them, and how you confirmed the adapter sequences.

6. Use ```Trimmomatic``` to quality trim your reads. Specify the following, in this order:
    - LEADING: quality of 3
    - TRAILING: quality of 3
    - SLIDING WINDOW: window size of 5 and required quality of 15
    - MINLENGTH: 35 bases

    Be sure to output compressed files and clear out any intermediate files.

7. Plot the trimmed read length distributions for both R1 and R2 reads (on the same plot). You can produce 2 different plots for your 2 different RNA-seq samples. There are a number of ways you could possibly do this. One useful thing your plot should show, for example, is whether R1s are trimmed more extensively than R2s, or vice versa. Comment on whether you expect R1s and R2s to be adapter-trimmed at different rates. 

# Part 3 – Alignment and strand-specificity
8. Install sofware. In your QAA environment, use conda to install:
    - star
    - numpy
    - pysam
    - matplotlib

    Then ```pip install HTSeq```

8. Find publicly available mouse genome fasta files (Ensemble release 104) and generate an alignment database from them. Align the reads to your mouse genomic database using a splice-aware aligner. Use the settings specified in PS8 from Bi621.

    *Hint* - you will need to use gene models to perform splice-aware alignment, see PS8 from Bi621.
    
9. Using your script from PS8 in Bi621, report the number of mapped and unmapped reads from each of your 2 sam files. Make sure that your script is looking at the bitwise flag to determine if reads are primary or secondary mapping (update your script if necessary).

10. Count reads that map to features using htseq-count. You should run htseq-count twice: once with ```--stranded=yes``` and again with ```--stranded=no```. Use default parameters otherwise.

11. Demonstrate convincingly whether or not the data are from “strand-specific” RNA-Seq libraries. Include any comands/scripts used. Briefly describe your evidence, using quantitative statements (e.g. "I propose that these data are/are not strand-specific, because X% of the reads are y, as opposed to z.").

    *Hint* - recall ICA4 from Bi621.

**To turn in your work for this assignment**:
Upload your Talapas batch script/code, FastQC plots, mapped/unmapped read counts, counts files generated from htseq-count, answers to questions, and any additional plots/code to github. You should create at most 2 files for submission (R markdown and the rendered pdf file) containing all these elements. The three parts of the assignment should be clearly labeled. Be sure to title and write a figure legend for each image/graph/table you present.
