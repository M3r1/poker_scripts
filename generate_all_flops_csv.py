import os
import glob

import all_flops
import flop_filter
import file_helper

ALL_FLOPS_CSV_FOLDER = "./ALL_FLOPS_CSVs/"
ALL_FLOPS_CSV_FILES = glob.glob(f"./{ALL_FLOPS_CSV_FOLDER}*")

for f in ALL_FLOPS_CSV_FILES:
    os.remove(f)

all_possible_flops = all_flops.get_all_flops_csv_arr()

monotone_file = open(f"{ALL_FLOPS_CSV_FOLDER}all_monotone_flops.csv", "x")
unpaired_rainbow_file = open(f"{ALL_FLOPS_CSV_FOLDER}all_unpaired_rainbow_flops.csv", "x")
paired_rainbow_file = open(f"{ALL_FLOPS_CSV_FOLDER}all_paired_rainbow_flops.csv", "x")
unpaired_two_tone_file = open(f"{ALL_FLOPS_CSV_FOLDER}all_unpaired_two_tone_flops.csv", "x")
paired_two_tone_file = open(f"{ALL_FLOPS_CSV_FOLDER}all_paired_two_tone_flops.csv", "x")
trips_file = open(f"{ALL_FLOPS_CSV_FOLDER}all_trips_flops.csv", "x")

file_helper.print_array_to_file(flop_filter.get_monotone_flops(all_possible_flops), monotone_file)
file_helper.print_array_to_file(flop_filter.get_unpaired_rainbow_flops(all_possible_flops), unpaired_rainbow_file)
file_helper.print_array_to_file(flop_filter.get_paired_rainbow_flops(all_possible_flops), paired_rainbow_file)
file_helper.print_array_to_file(flop_filter.get_unpaired_two_tone_flops(all_possible_flops), unpaired_two_tone_file)
file_helper.print_array_to_file(flop_filter.get_paired_two_tone_flops(all_possible_flops), paired_two_tone_file)
file_helper.print_array_to_file(flop_filter.get_trips_flops(all_possible_flops), trips_file)

monotone_file.close()
unpaired_rainbow_file.close()
paired_rainbow_file.close()
unpaired_two_tone_file.close()
paired_two_tone_file.close()
trips_file.close()