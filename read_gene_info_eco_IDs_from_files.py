path = "input_folder"
def file_reader(input_file_name, seperator, geneColumn, infoColumn, ecoColumn):
    gene_info_ecoID_Dict = dict()
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
                info = line_list[infoColumn].strip()
                if gene_id not in gene_info_ecoID_Dict:
                    gene_info_ecoID_Dict[gene_id] = dict()
                gene_info_ecoID_Dict[gene_id][info] = set()
                eco_id = line_list[ecoColumn].strip()
                gene_info_ecoID_Dict[gene_id][info].add(eco_id)
    fp.close()

    return gene_info_ecoID_Dict


gene_info_ecoID_Dict =  file_reader("sample_input.txt", "tab", 1, 4, 6)
print(gene_info_ecoID_Dict["A0A1B0GTQ4"]["GO:0005789"])

