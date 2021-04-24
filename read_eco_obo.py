def read_ecoObo():
    file_ = open("eco.obo", "r")
    eco_term_dict= dict()
    eco_id=""
    for line in file_:
        parts = line.split(": ")
        if parts[0] == "id":
            eco_id = parts[1].strip()
            if eco_id != "" and eco_id not in eco_term_dict:
                eco_term_dict[eco_id] = list()
        elif parts[0] == "is_a":
            parts_is_a = parts[1][0:11]
            eco_term_dict[eco_id].append(parts_is_a.strip())

    return eco_term_dict
