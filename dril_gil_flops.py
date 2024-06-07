import glob
import random
from helpers import file_helper
from combos import hands

ALL_ANALYSIS_CSV_FOLDER = "./Data/GIL_FLOPS/LJ_vs_BTN/LJ/UNPAIRED_TWO_TONE/"
ALL_ANALYSIS_CSV_FILES = glob.glob(f"{ALL_ANALYSIS_CSV_FOLDER}*")
DRILL_HANDS = False

def verify_user_input(prompt_message, correct_value):
    input_value = str(input(f"{prompt_message}\n"))

    if input_value == correct_value:
        print("Correct, Great Job!!!")
        return True
    else:
        print(f"Wrong, the answer is: {correct_value}")
        return False
    
def get_analyze_dict(combo, hand_strength, check_or_bet):
    return {
        "combo": combo,
        "hand_strength": hand_strength,
        "action": check_or_bet
    }

def create_analyze_dict_entry(hand_strength, symbols_field, check_or_bet):
    analyzed_hands_dict_array = []

    for symbol in symbols_field.split(","):
        if symbol != "":
            analyzed_hands_dict_array.append(get_analyze_dict(symbol, hand_strength, check_or_bet))

    return analyzed_hands_dict_array

# while True:
number_of_flops = len(ALL_ANALYSIS_CSV_FILES)
random_index_options = list(range(number_of_flops))

for _ in range(number_of_flops):
    random_int = random.randint(0, len(random_index_options) - 1)
    random_index = random_index_options[random_int]
    random_index_options.pop(random_int)

    analysis_matrix = file_helper.get_csv_matrix(ALL_ANALYSIS_CSV_FILES[random_index])
    flop_name = ALL_ANALYSIS_CSV_FILES[random_index].split("/")[-1].split("\\")[1].split(".")[0]

    check_percentage = "1" if analysis_matrix[0][0] == "Check 100%" else str(analysis_matrix[-1][2])
    
    while not verify_user_input(f"On flop {flop_name} what percentage of my range should I check?", check_percentage): pass

    if check_percentage != "1":
        while not verify_user_input(f"On flop {flop_name} what bet size should I use?", str(analysis_matrix[0][1][4:6])): pass

        if DRILL_HANDS:
            combo_dict = hands.get_combo_dict()
            analyzed_combo_dict = []

            for row_array in analysis_matrix[1:-1]:
                analyzed_combo_dict = analyzed_combo_dict + create_analyze_dict_entry(row_array[0], row_array[1], "Check")
                analyzed_combo_dict = analyzed_combo_dict + create_analyze_dict_entry(row_array[0], row_array[2], "Bet")

            for entry in analyzed_combo_dict:
                while not verify_user_input(f"On flop {flop_name} what should I do with {entry['combo']}-{entry['hand_strength']}?", entry["action"]): pass
                            
