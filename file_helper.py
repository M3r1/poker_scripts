import csv

def print_array_to_file(arr, file):
    for item in arr:
        file.write(f"{item}\n")

def get_array_of_file_lines(file):
    arr = []
    for row in file:
        if row.strip() != None:
            arr.append(row.strip())

    return arr