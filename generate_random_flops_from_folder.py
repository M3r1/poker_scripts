import file_helper
import glob
import random

PERCENTAGE_FROM_EACH_CATEGORY = "0.4"

FLOPS_DIR = "./TIPTON_FLOPS/"
ALL_FLOPS_CSV_FILES = glob.glob(f"{FLOPS_DIR}*")

for flop_file_path in ALL_FLOPS_CSV_FILES:
    flop_file = open(flop_file_path, "r")
    flops = file_helper.get_array_of_file_lines(flop_file)

    number_of_flops = max(1, round(len(flops) * 0.25))

    print(f"#### {flop_file_path} ####")
    for _ in range(number_of_flops):
        print(flops[random.randint(0, len(flops) - 1)])
    
    print(f"##########################")
    print()
    print()
    flop_file.close()