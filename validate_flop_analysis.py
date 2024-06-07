import glob
from helpers import file_helper, flopzilla_helper
from combos import combo_pool, hands

def remove_combo_from_range(symbol, hand, player_possilbe_combos, flop_name, flop_cards):
    reverse_hand = f"{hand[2:4]}{hand[0:2]}"

    if symbol[0] not in hands.ANALYZE_SYMBOLS:
        if hand[0:2] in flop_cards or hand[2:4] in flop_cards:
            print(f"{hand} in {flop_name} contains a card that is part of the flop")
            raise Exception()

    if hand in player_possilbe_combos:
        player_possilbe_combos.remove(hand)
    elif reverse_hand in player_possilbe_combos:
        player_possilbe_combos.remove(reverse_hand)
    else:
        print(f"{hand} in {flop_name} is either not in the player's range or is written twice")
        raise Exception()

PLAYER_RANGE = "[100]AA[/100],[100]AKs[/100],[100]AQs[/100],[100]AJs[/100],[100]ATs[/100],[100]A9s[/100],[100]A8s[/100],[100]A7s[/100],[100]A6s[/100],[100]A5s[/100],[100]A4s[/100],[100]A3s[/100],[100]A2s[/100],[100]AKo[/100],[100]KK[/100],[100]KQs[/100],[100]KJs[/100],[100]KTs[/100],[100]K9s[/100],[100]K8s[/100],[75]K7s[/75],[100]K6s[/100],[81]K5s[/81],[100]AQo[/100],[100]KQo[/100],[100]QQ[/100],[100]QJs[/100],[100]QTs[/100],[100]Q9s[/100],[20]Q8s[/20],[100]AJo[/100],[100]KJo[/100],[67]QJo[/67],[100]JJ[/100],[100]JTs[/100],[100]ATo[/100],[26]KTo[/26],[4]QTo[/4],[100]TT[/100],[23]T9s[/23],[100]99[/100],[10]98s[/10],[100]88[/100],[10]87s[/10],[75]77[/75],[11]76s[/11],[26]66[/26],[18]65s[/18],[16]55[/16],[8]54s[/8],[16]44[/16],[18]33[/18],[17]22[/17]"
ALL_ANALYSIS_CSV_FOLDER = "./Data/GIL_FLOPS/LJ_vs_BTN/LJ/UNPAIRED_TWO_TONE/"

ALL_ANALYSIS_CSV_FILES = glob.glob(f"{ALL_ANALYSIS_CSV_FOLDER}*")

all_hand_symbols = []

for analysis_file_path in ALL_ANALYSIS_CSV_FILES:
    analysis_matrix = file_helper.get_csv_matrix(analysis_file_path)
    flop_name = analysis_file_path.split("/")[-1].split("\\")[1].split(".")[0]

    if analysis_matrix[0][0] != "Check 100%":
        hand_symbols = []

        if analysis_matrix[-1][0] != "Total":
            raise Exception("Last row of csv analysis doesn't contain Total")
        
        for row_array in analysis_matrix:
            if len(row_array) < 3:
                print(f"Missing field in one of the rows of {flop_name} analysis file")
                raise Exception("Missing Field")
            
        for row_array in analysis_matrix[1:-1]:
            for field in row_array[1:]:
                for hand_symbol in field.split(","):
                    if hand_symbol != "":
                        if len(hand_symbol) != 3 and len(hand_symbol) != 4:
                            print(f"One of the hands in {flop_name} analysis file is written wrong: {hand_symbol}")
                            raise Exception("Bad Hand Format")
                        else:
                            hand_symbols.append(hand_symbol)

        all_hand_symbols.append(
            {
                "flop_name": flop_name,
                "hand_symbols": hand_symbols
            }
        )

all_combos_in_range = flopzilla_helper.get_flat_range_from_flopzilla_range(PLAYER_RANGE)

for flop_hand_symbols_dict in all_hand_symbols:
    hand_symbols = flop_hand_symbols_dict["hand_symbols"]
    flop_name = flop_hand_symbols_dict["flop_name"]
    flop_cards = [flop_name[0:2], flop_name[2:4], flop_name[4:6]]

    if flop_cards[0][0] not in hands.RANKS or flop_cards[1][0] not in hands.RANKS or flop_cards[2][0] not in hands.RANKS or \
        flop_cards[0][1] not in hands.SUITS or flop_cards[1][1] not in hands.SUITS or flop_cards[2][1] not in hands.SUITS:
        print(f"Bad flop file name format for flop: {flop_name}")
        raise Exception()

    combo_dict = hands.get_combo_dict()
    flat_range = flopzilla_helper.get_flat_range_from_flopzilla_range(PLAYER_RANGE)
    
    player_possilbe_combos = list(combo_pool.build_flat_combo_pool(flat_range))

    for symbol in hand_symbols:
        if symbol[0] not in hands.RANKS and symbol[0] not in hands.ANALYZE_SYMBOLS:
            print(f"Found a symbol {symbol} that is formatted wrong in {flop_name}")
            raise Exception()
        
        if len(symbol) == 4:
            if symbol[0] not in hands.RANKS or symbol[2] not in hands.RANKS or \
                symbol[1] not in hands.SUITS or symbol[3] not in hands.SUITS:
                print(f"Found a symbol {symbol} that is formatted wrong in {flop_name}")
                raise Exception()

        if symbol[0] == "a":
            if symbol[1] == symbol[2]:
                for hand in combo_dict[symbol[1:3]]:
                    remove_combo_from_range(symbol, hand, player_possilbe_combos, flop_name, flop_cards)
            else:
                for hand in combo_dict[f"{symbol[1:]}o"]:
                    remove_combo_from_range(symbol, hand, player_possilbe_combos, flop_name, flop_cards)
                for hand in combo_dict[f"{symbol[1:]}s"]:
                    remove_combo_from_range(symbol, hand, player_possilbe_combos, flop_name, flop_cards)
        elif symbol[0] == "s":
            for hand in combo_dict[f"{symbol[1:]}s"]:
                remove_combo_from_range(symbol, hand, player_possilbe_combos, flop_name, flop_cards)
        elif symbol[0] == "o":
            for hand in combo_dict[f"{symbol[1:]}o"]:
                remove_combo_from_range(symbol, hand, player_possilbe_combos, flop_name, flop_cards)
        else:
            remove_combo_from_range(symbol, symbol, player_possilbe_combos, flop_name, flop_cards)

    player_possilbe_combos_clone = player_possilbe_combos.copy()

    for combo in player_possilbe_combos_clone:
        if combo[0:2] in flop_cards or combo[2:4] in flop_cards:
            player_possilbe_combos.remove(combo)

    if len(player_possilbe_combos) > 0:
        print(f"The following hand combos are not written in flop {flop_name}:")
        print(player_possilbe_combos)
        raise Exception()
    
print("All flops were successfully validated")
