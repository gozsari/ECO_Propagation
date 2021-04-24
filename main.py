from propagate_eco import form_all_eco_parents_dict
from read_eco_obo import read_ecoObo
from read_gene_info_eco_IDs_from_files import file_reader
from write_to_file import write_to_file
import argparse

parser = argparse.ArgumentParser(description='Go_Propagation arguments')
parser.add_argument(
    '--inputFile',
    type=str,
    default="input",
    help='genes/protein, info and eco_terms input_file_name, input file name should be written with extension such as .txt, .csv')
parser.add_argument(
    '--seperator',
    type=str,
    default="space",
    help='seperator of input file columns, default it is space, other options can be tab or commo')
parser.add_argument(
    '--geneColumn',
    type=int,
    default=0,
    help='gene/protein column number in the input file, starting index = 0')
parser.add_argument(
    '--infoColumn',
    type=int,
    default=1,
    help='info column number in the input file, starting index = 0')
parser.add_argument(
    '--ecoColumn',
    type=int,
    default=1,
    help='evidence code(eco) column number in the input file, starting index = 0')
parser.add_argument(
    '--outEco',
    type=str,
    default="ECO:0000000",
    help='evidence code(eco) for output file')
if __name__ == "__main__":
    args = parser.parse_args()
    input_file_name = args.inputFile
    seperator = args.seperator

    geneColumn = args.geneColumn
    ecoColumn = args.ecoColumn
    infoColumn = args.infoColumn
    gene_info_ecoID_Dict = file_reader(input_file_name, seperator, geneColumn, infoColumn, ecoColumn)
    eco_term_dict = read_ecoObo()
    eco_parents_dict = form_all_eco_parents_dict(eco_term_dict)

    all_gene_info_ecoIDs_propagated = dict()
    for gene_id in gene_info_ecoID_Dict:
        if gene_id not in all_gene_info_ecoIDs_propagated:
            all_gene_info_ecoIDs_propagated[gene_id] = dict()
        for info in gene_info_ecoID_Dict[gene_id]:
            eco_list = set()
            for eco_id in gene_info_ecoID_Dict[gene_id][info]:
                eco_list.add(eco_id)
                for parent_ecoID in eco_parents_dict[eco_id]:
                    eco_list.add(parent_ecoID)
            all_gene_info_ecoIDs_propagated[gene_id][info] = eco_list
    output_eco = args.outEco
    write_to_file(input_file_name, all_gene_info_ecoIDs_propagated, output_eco)

