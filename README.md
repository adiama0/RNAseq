# RNA-Seq Analysis Pipeline  

This repository contains a Snakemake-based RNA-Seq analysis pipeline designed to process raw sequencing data, perform quality control, align reads to a reference genome, quantify gene expression, and conduct differential expression analysis. The pipeline also includes downstream analyses such as Gene Set Enrichment Analysis (GSEA), Principal Component Analysis (PCA), and functional enrichment analysis.  

---

## Table of Contents  
1. [Overview](#overview)  
2. [Pipeline Workflow](#pipeline-workflow)  
3. [Dependencies](#dependencies)  
4. [Usage](#usage)  
5. [Results and Deliverables](#results-and-deliverables)  
6. [Questions to Address](#questions-to-address)  
7. [Acknowledgments](#acknowledgments)  

---

## Overview  

This project analyzes RNA-Seq data from 6 samples: 3 Wild-Type (WT) and 3 Knockout (KO) samples derived from a human source. The pipeline performs the following steps:  
1. **Quality Control**: FastQC and MultiQC are used to assess the quality of raw sequencing reads.  
2. **Alignment**: Reads are aligned to the human reference genome (GRCh38) using STAR.  
3. **Gene Quantification**: Gene counts are generated using VERSE.  
4. **Differential Expression Analysis**: DESeq2 is used to identify differentially expressed genes between WT and KO conditions.  
5. **Downstream Analysis**: GSEA, PCA, and functional enrichment analysis are performed to interpret the results.  

---

## Pipeline Workflow  

The pipeline consists of the following steps:  

1. **Download Reference Genome and Annotation**:  
   - The human reference genome (GRCh38) and GTF annotation file are downloaded from the GENCODE database.  

2. **Quality Control**:  
   - FastQC is used to generate quality reports for each sample.  
   - MultiQC aggregates the FastQC reports into a single summary.  

3. **Genome Indexing**:  
   - STAR is used to build a genome index for alignment.  

4. **Alignment**:  
   - Reads are aligned to the reference genome using STAR, producing unsorted BAM files.  

5. **Alignment Quality Control**:  
   - Samtools flagstat is used to generate alignment statistics.  

6. **Gene Quantification**:  
   - VERSE is used to generate gene counts from the aligned reads.  

7. **Count Matrix Filtering**:  
   - A custom Python script (`concatenate_filter.py`) combines and filters gene counts to remove genes with zero counts across all samples.  

8. **Differential Expression Analysis**:  
   - DESeq2 is used to identify differentially expressed genes between WT and KO conditions.  

9. **Downstream Analysis**:  
   - GSEA is performed using the fgsea package and the MSigDB C2 canonical pathways collection.  
   - PCA is performed to visualize sample variance.  
   - Functional enrichment analysis is conducted using EnrichR.  

---

## Dependencies  

The pipeline requires the following software and tools, managed via Conda environments:  

### Core Dependencies  
- **Snakemake**: Workflow management.  
- **Python**: For custom scripts and data processing.  
- **R**: For differential expression and downstream analysis.  

### Conda Environments  
The pipeline uses several Conda environments defined in the `envs/` folder:  
- `fastqc_env.yml`: FastQC for quality control.  
- `multiqc_env.yml`: MultiQC for report aggregation.  
- `samtools_env.yml`: Samtools for alignment statistics.  
- `star_env.yml`: STAR for alignment and genome indexing.  
- `verse_env.yml`: VERSE for gene quantification.  
- `base_end.yml`: Base environment for Snakemake and Python.  

---

## Usage  

To run the pipeline:  

1. Ensure Conda and Snakemake are installed.  
2. Clone this repository and navigate to the project directory.  
3. Run the pipeline using the following command:
```bash
snakemake --use-conda --cores <number_of_cores>
```
Replace `<number_of_cores>` with the desired number of CPU cores.

## Results and Deliverables  

The pipeline generates the following outputs:  

1. **Quality Control Reports**:  
   - FastQC reports for each sample.  
   - MultiQC summary report (`results/multiqc_report.html`).  

2. **Alignment Statistics**:  
   - Samtools flagstat reports (`results/flagstat/`).  

3. **Gene Count Matrix**:  
   - Filtered gene count matrix (`results/filtered_matrix.csv`).  

4. **Differential Expression Results**:  
   - DESeq2 results (`results/differential_expression/`).  
   - Histogram of log2FoldChange distribution.  
   - Volcano plot highlighting significant genes.  

5. **Downstream Analysis Results**:  
   - GSEA results for MSigDB C2 pathways.  
   - PCA plot visualizing sample variance.  
   - EnrichR functional enrichment results.  

---

## Questions to Address  

### Quality Control  
1. **Sequencing Reads**:  
   - Are there any concerning aspects of the quality control of your sequencing reads?  
   - Are there any samples with low-quality reads that should be excluded?  

2. **Alignment Statistics**:  
   - Are there any concerning aspects of the alignment quality?  
   - Based on the alignment statistics, will you exclude any samples from further analysis?  

### Differential Expression Analysis  
1. **PCA Plot**:  
   - What does the PCA plot indicate about the biological variance between samples?  
   - Does the plot suggest a clear separation between WT and KO conditions?  

2. **Differential Expression Results**:  
   - How many genes are significantly differentially expressed at your chosen FDR threshold?  
   - What are the top 10 most significant genes, and how do they relate to the experimental conditions?  

3. **GSEA and Enrichment Analysis**:  
   - How do the results from GSEA compare to the functional enrichment analysis using EnrichR?  
   - Are there any notable differences, and if so, why?  

---

## Acknowledgments  

This project was completed as part of the BF528 course at [Boston University]. Special thanks to the instructor Joey Orofino for their guidance and support.  

