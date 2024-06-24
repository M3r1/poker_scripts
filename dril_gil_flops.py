import glob
import random
from helpers import file_helper

ALL_ANALYSIS_CSV_FOLDER = "./Data/GIL_FLOPS/LJ_vs_BTN/LJ/Monotone/"
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

# while True:
number_of_flops = len(ALL_ANALYSIS_CSV_FILES)
random_index_options = list(range(number_of_flops))

for _ in range(number_of_flops):
    random_int = random.randint(0, len(random_index_options) - 1)
    random_index = random_index_options[random_int]
    random_index_options.pop(random_int)

    analysis_matrix = file_helper.get_csv_matrix(ALL_ANALYSIS_CSV_FILES[random_index])
    flop_name = ALL_ANALYSIS_CSV_FILES[random_index].split("/")[-1].split("\\")[1].split(".")[0]

    check_percentage = "100" if analysis_matrix[0][0] == "Check 100%" else str(analysis_matrix[-1][-1])
    
    while not verify_user_input(f"On flop {flop_name} what percentage of my range should I check?", check_percentage): pass

    if check_percentage != "100":
        bet_sizes = analysis_matrix[0][1:-1]
        bet_sizes = [float(size[0:-1]) for size in bet_sizes]
        bet_sizes_clone = bet_sizes.copy()

        while len(bet_sizes) > 0:
            input_value = str(input(f"On flop {flop_name} what bet sizes should I use?\n"))

            if float(input_value) in bet_sizes:
                print("Correct")

                bet_sizes.remove(float(input_value))
            else:
                print("Wrong")

        print(f"Good job, on flop: {flop_name}, {bet_sizes_clone} bet sizes are recommended")
