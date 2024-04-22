# RNAseq
BF528 Project

## Methods
This dataset consists of 6 samples: 3 WT and 3 KO derived from a human source. Initial quality control was performed using FastQC v0.12.0 and visualized through MultiQC v1.17. Genome index was assembled using STAR v2.7.11b: overhang set as 99, the rest of the parameters were set as default. GTF and Fasta genome files were sourced from the gencode human database. Reads were aligned to the built genome index using STAR: output file was selected as unsorted BAM files, all other parameters remained default. Alignment QC was performed using samtools flagstats tool (v1.19.2). Gene counts was then generated from alignments using VERSE v0.1.5 with default parameters and the gencode GRCh38 primary assembly GTF. Counts were combined and filtered to remove genes that did not have a non-zero count in all 6 samples using an auxiliary phython code (v3.9). Normalization and differential expression analysis was performed with DESeq2 (v1.36.0) using default parameters comparing the WT and KO sample conditions. GSEA analysis was perfomed using fgsea package (v1.22.0). The C2 gene pathway collection was sourced from the human database for GSEA. PCA (v2.22.0) was performed on the samples using the countmatrix and countdata variables in order to visualize variance. Enrichment analysis was performed using enrichR (v3.2) using GO_Biological_Process_2023 gene set library on selected genes ("MTHFR", "CD52", "CYP4Z1", "TP73", "AURKAIP1", "MTOR", "MYCBP", "PIK3CD"). Genes were selected based on differential expression and relevance from GSEA analysis. 

## Questions to Address
Briefly remark on the quality of the sequencing reads and the alignment statistics, make sure to specifically mention the following:
  - Are there any concerning aspects of the quality control of your sequencing reads?
  - Are there any concerning aspects of the quality control related to alignment?
  - Based on all of your quality control, will you exclude any samples from further analysis?

Perform either a PCA or sample distance analysis on the counts matrix (refer to the DESeq2 vignette)
  - Remark on the plot and what it indicates to you in terms of the success of the experiment

Choose an appropriate FDR threshold to subset the differential expression results
  - How many genes are significantly differentially expressed at your chosen threshold?

Compare the results from the GSEA analysis to the gene enrichment analysis using just the DE genes (DAVID, EnrichR)
  - How similar are the results? Are there any notable differences?
  - Do you expect there to be any differences? If so, why?

    
## Deliverables
Produce either of the following: 
1. A sample-to-sample distance plot or a PCA plot
2. A CSV of all of the results from DESeq2
3. A histogram showing the distribution of log2fold changes from your DE genes
4. A volcano plot that clearly distinguishes between significant and non-significant genes as well as whether those genes are
   up- or downregulated based on their log2foldchange. 
    - Label the top ten most significant genes on the plot
6. Perform GSEA analysis on all of the genes discovered in the experiment
    - You may choose an appropriate ranking metric
    - Report the results you believe are most interesting in a single table / figure
    - You may use the MSIGDB C2 canonical pathways collection or one of your choice
7. Use the same thresholded DE results and perform a basic enrichment analysis using a well-known annotation tool such
   as DAVID or enrichR
     - Report the results you believe are most interesting in a single table / figure
