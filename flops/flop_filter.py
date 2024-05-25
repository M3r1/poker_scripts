import random

import flops.flop_category as flop_category

def get_monotone_flops(all_possible_flops):
    return [flop for flop in all_possible_flops if flop_category.is_monotone(flop)]

def get_distinct_random_monotone_flops(all_possible_flops):
    all_monotone_flops = get_monotone_flops(all_possible_flops)
    return get_distinct_random_flops(all_monotone_flops)

def get_paired_rainbow_flops(all_possible_flops):
    return [flop for flop in all_possible_flops if flop_category.is_paired_rainbow(flop)]

def get_distinct_random_paired_rainbow_flops(all_possible_flops):
    all_paired_rainbow_flops = get_paired_rainbow_flops(all_possible_flops)
    return get_distinct_random_flops(all_paired_rainbow_flops)

def get_paired_two_tone_flops(all_possible_flops):
    return [flop for flop in all_possible_flops if flop_category.is_paired_two_tone(flop)]

def get_distinct_random_paired_two_tone_flops(all_possible_flops):
    all_paired_two_tone_flops = get_paired_two_tone_flops(all_possible_flops)
    return get_distinct_random_flops(all_paired_two_tone_flops)

def get_trips_flops(all_possible_flops):
    return [flop for flop in all_possible_flops if flop_category.is_trips(flop)]

def get_distinct_random_trips_flops(all_possible_flops):
    all_trips_flops = get_trips_flops(all_possible_flops)
    return get_distinct_random_flops(all_trips_flops)

def get_unpaired_rainbow_flops(all_possible_flops):
    return [flop for flop in all_possible_flops if flop_category.is_unpaired_rainbow(flop)]

def get_distinct_random_unpaired_rainbow_flops(all_possible_flops):
    all_upaired_rainbow_flops = get_unpaired_rainbow_flops(all_possible_flops)
    return get_distinct_random_flops(all_upaired_rainbow_flops)

def get_unpaired_two_tone_flops(all_possible_flops):
    return [flop for flop in all_possible_flops if flop_category.is_unpaired_two_tone(flop)]

def get_distinct_random_unpaired_two_tone_flops(all_possible_flops):
    all_unpaired_two_tone_flops = get_unpaired_two_tone_flops(all_possible_flops)
    return get_distinct_random_flops(all_unpaired_two_tone_flops)

def get_distinct_random_flops(all_possible_flops):
    flops_dict_by_ranks = {}
    
    for flop in all_possible_flops:
        flop_ranks_key = f"{flop[0]}, {flop[4]}, {flop[8]}"
        
        if flop_ranks_key not in flops_dict_by_ranks:
            flops_dict_by_ranks[flop_ranks_key] = [flop]
        else:
            flops_dict_by_ranks[flop_ranks_key].append(flop)

    return [flops_dict_by_ranks[rank][random.randrange(len(flops_dict_by_ranks[rank]))] for rank in flops_dict_by_ranks]