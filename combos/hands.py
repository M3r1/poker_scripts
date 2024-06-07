from itertools import combinations

ANALYZE_SYMBOLS = ["a", "s", "o"]

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
STRENGTH_DICT = {
    '2': 0,
    '3': 1, 
    '4': 2, 
    '5': 3, 
    '6': 4, 
    '7': 5, 
    '8': 6, 
    '9': 7, 
    'T': 8, 
    'J': 9, 
    'Q': 10, 
    'K': 11, 
    'A': 12
}
SUITS = ['h', 'd', 'c', 's']

def get_deck():
    return [f"{rank}{suit}" for rank in RANKS for suit in SUITS]

def get_all_combos_arr():
    all_combos_raw = list(combinations(get_deck(), 2))

    all_combos = []
    for flop_tuple in all_combos_raw:
        if STRENGTH_DICT[flop_tuple[0][0]] > STRENGTH_DICT[flop_tuple[1][0]]:
            all_combos.append(f"{flop_tuple[0]}{flop_tuple[1]}")
        else:
            all_combos.append(f"{flop_tuple[1]}{flop_tuple[0]}")

    return all_combos

def get_combo_dict():
    all_combos = get_all_combos_arr()

    combo_dict = {}
    for combo in all_combos:
        if combo[0] == combo[2]:
            combo_key = f"{combo[0]}{combo[2]}"
        elif combo[1] == combo[3]:
            combo_key = f"{combo[0]}{combo[2]}s"
        else:
            combo_key = f"{combo[0]}{combo[2]}o"

        if combo_key not in combo_dict:
            combo_dict[combo_key] = [combo]
        else:
            combo_dict[combo_key].append(combo)

    return combo_dict