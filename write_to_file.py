def write_to_file(file_name, all_gene_goIDs_propagated, output_eco):
    file_name_ = file_name.split('.')[0]
    with open("{}/{}_propagated_genes_info_ecoIDs.csv".format("output_folder", file_name_), "w") as fw:
        fw.write("GENE_ID, INFO, EVIDENCE\n")
        for gene_id in all_gene_goIDs_propagated:
            for info in all_gene_goIDs_propagated[gene_id]:
                for eco in all_gene_goIDs_propagated[gene_id][info]:
                    if eco == output_eco:
                        fw.write("{}, {}, {}\n".format(gene_id, info, output_eco))
    fw.close()