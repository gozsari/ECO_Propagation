def write_to_file(file_name, all_gene_annotation_ecoIDs_propagated, output_eco):
    file_name_ = file_name.split('.')[0]
    with open("{}/{}_propagated_genes_annotation_ecoIDs.csv".format("output_folder", file_name_), "w") as fw:
        fw.write("GENE_ID, ANNOTATION, EVIDENCE\n")
        for gene_id in all_gene_annotation_ecoIDs_propagated:
            for annotation in all_gene_annotation_ecoIDs_propagated[gene_id]:
                for eco in all_gene_annotation_ecoIDs_propagated[gene_id][annotation]:
                    if eco == output_eco:
                        fw.write("{}, {}, {}\n".format(gene_id, annotation, output_eco))
    fw.close()