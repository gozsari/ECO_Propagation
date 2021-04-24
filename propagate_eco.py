def propagate_eco(eco_id, parent_set, eco_term_dict):
    if len(eco_term_dict[eco_id]) == 0:
        return parent_set
    for parent in eco_term_dict[eco_id]:
        parent_set.add(parent)

    for parent in eco_term_dict[eco_id]:
        propagate_eco(parent, parent_set, eco_term_dict)
    return parent_set

def form_all_eco_parents_dict(eco_term_dict):
    eco_parents_dict = dict()
    for eco_id in eco_term_dict:
        parent_set = set()
        parent_set = propagate_eco(eco_id, parent_set, eco_term_dict)
        eco_parents_dict[eco_id] = parent_set
    return eco_parents_dict

