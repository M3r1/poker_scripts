import random
from . import hands

def build_weighted_combo_pool(range_weight_dict):
    total_combos_available_by_weight = []

    for combo in range_weight_dict:
        for _ in range(range_weight_dict[combo]):
            total_combos_available_by_weight.append(combo)

    return total_combos_available_by_weight

def build_flat_combo_pool(flopzilla_combos_symbols):
    combo_dict = hands.get_combo_dict()
    
    combo_pool = []
    for combo_symbol in flopzilla_combos_symbols:        
        combo_pool = combo_pool + combo_dict[combo_symbol]

    return combo_pool


def get_unique_combos_from_combo_pool(range_weight_dict, combos_to_generate):
    commbo_dict = hands.get_combo_dict()

    unique_combos = []
    for _ in range(combos_to_generate):
        combo_pool = build_weighted_combo_pool(range_weight_dict)
    
        random_combo = combo_pool[random.randint(0, len(combo_pool) - 1)]
        range_weight_dict.pop(random_combo)
    
        unique_combos.append(commbo_dict[random_combo][random.randint(0, len(commbo_dict[random_combo]) - 1)])

    return unique_combos