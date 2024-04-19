import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help='The input file specified will be the GTF file provided by snakemake',dest="input", required=True)
parser.add_argument("-o", "--output", help='The output file name and path provided by snakemake',dest="output", required=True)

args = parser.parse_args()

print(args.input)
print(args.output)

def extract_gene_info(attributes):
    # initialize the attributes to none 
    gene_id = None
    gene_name = None
    
    # Split attributes by semicolon to get individual key-value pairs
    attribute_pairs = attributes.split(';')
    
    # Iterate through each key-value pair
    for pair in attribute_pairs:
        # Strip leading/trailing whitespaces
        pair = pair.strip()
        # Split each pair by whitespace to separate key and value
        key_value = pair.split(' ')
        # Check if the key-value pair contains both key and value
        if len(key_value) >= 2:
            key = key_value[0].strip()
            value = ' '.join(key_value[1:]).strip('"')
            if key == 'gene_id':
                gene_id = value
            elif key == 'gene_name':
                gene_name = value
            
    return gene_id, gene_name

# Open input GTF file
with open(args.input, 'r') as gtf_file:
    # Open output file for writing
    with open(args.output, 'w') as output_file:
        # Iterate through each line in the GTF file
        for line in gtf_file:
            # Skip comment lines
            if line.startswith('#'):
                continue
            # Split the line by tabs to separate columns
            columns = line.strip().split('\t')
            
            # Extract feature type and attributes
            feature_type = columns[2]
            attributes = columns[8]
            
            # extract gene ID and gene name
            if feature_type == 'gene':
                gene_id, gene_name = extract_gene_info(attributes)
                # Write gene ID and gene name to the output file
                if gene_id and gene_name:
                    output_file.write(f"{gene_id},{gene_name}\n")
