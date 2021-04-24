path = "input_folder"
def file_reader(input_file_name, seperator, geneColumn, annotationColumn, ecoColumn):
    gene_annotation_ecoID_Dict = dict()
    if seperator=="commo":
        seperator = ","
    elif seperator== "tab":
        seperator = "\t"
    elif seperator == "space":
        seperator = " "
    with open("{}/{}".format(path, input_file_name), mode="r") as fp:
        for i, line in enumerate(fp):
            line_list = (line.strip().split(seperator))
            #First line is assumed to be identification line for each column
            if i > 0:
                gene_id = line_list[geneColumn].strip()
                annotation = line_list[annotationColumn].strip()
                if gene_id not in gene_annotation_ecoID_Dict:
                    gene_annotation_ecoID_Dict[gene_id] = dict()
                gene_annotation_ecoID_Dict[gene_id][annotation] = set()
                eco_id = line_list[ecoColumn].strip()
                gene_annotation_ecoID_Dict[gene_id][annotation].add(eco_id)
    fp.close()

    return gene_annotation_ecoID_Dict



