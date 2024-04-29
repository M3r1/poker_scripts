import re

def get_range_weight_dict_from_flopzilla_range(flopzilla_range):
    entries = flopzilla_range.split(",")

    flopzilla_entry_pattern = r'\[(\d+)\]([^\[]+)\[\/\1\]'

    range_weight_dict = {}
    for entry in entries:
        match = re.search(flopzilla_entry_pattern, entry)
        range_weight_dict[match.group(2)] = int(match.group(1))

    return range_weight_dict