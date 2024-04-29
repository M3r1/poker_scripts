from itertools import combinations

import hands

def get_all_flops_tuple_list():
    return list(combinations(hands.get_deck(), 3))

def get_all_flops_csv_arr():
    return [f"{flop_tuple[0]}, {flop_tuple[1]}, {flop_tuple[2]}" for flop_tuple in get_all_flops_tuple_list()]