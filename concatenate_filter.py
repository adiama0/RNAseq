import argparse
import pandas as pd

# Initialize the argparse object that we will modify
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help='A list of the VERSE output filenames provided by snakemake', dest="input", required=True, nargs='+')
parser.add_argument("-o", "--output", help='The output file name and path provided by snakemake', dest="output", required=True)
parser.add_argument("-t", "--temp", help='The temporary file to store unfiltered count matrix', dest="temp", required = True)

# this method will run the parser and input the data into the namespace object
args = parser.parse_args()

print(args.input)
print(args.output)
print(args.temp)

def concatenate_files(input_files, output_file):
    # Initialize an empty DataFrame to store concatenated files
    concatenated_data = pd.DataFrame()
    # Initialize a list to store gene columns
    gene_columns = []
    
    # Iterate through each input file
    for file in input_files:
        # Read the file
        data = pd.read_csv(file, sep='\t')
        # Extract the gene column and store it
        gene_columns.append(data['gene'])
        # Drop the gene column from the DataFrame
        data = data.drop(columns=['gene'])
        # Extract the input file name
        file_name = file.split('/')[-1].split('.')[0]
        # Rename the 'count' column to the input file name
        data = data.rename(columns={'count': file_name})
        # Concatenate the remaining data
        concatenated_data = pd.concat([concatenated_data, data], axis=1)
    
    # Concatenate the gene columns along the columns axis
    gene_data = pd.concat(gene_columns, axis=1)
    # Add the gene data to the concatenated DataFrame
    concatenated_data = pd.concat([gene_data.iloc[:, 0], concatenated_data], axis=1)
    
    # Write the concatenated DataFrame to a CSV file
    concatenated_data.to_csv(output_file, index=False)

def filter_count_matrix(input_file, output_file):
    # Read the count matrix file
    count_matrix = pd.read_csv(input_file)
    
    # Filter rows with all zero counts
    non_zero_count_matrix = count_matrix[(count_matrix.iloc[:, 1:] != 0).any(axis=1)]
    
    # Write the filtered count matrix to a CSV file
    non_zero_count_matrix.to_csv(output_file, index=False)

# Run the function to concatenate the input files into the count matrix
concatenate_files(args.input, args.temp)

# Run the function to filter the count matrix and output the filtered count matrix
filter_count_matrix(args.temp, args.output)
