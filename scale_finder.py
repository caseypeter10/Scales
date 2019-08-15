import scl
def scale_finder(key, notes):
    # generates major_scale based on filtering a list returned by the string_prep
    # function

    organized_on_key = scl.string_prep(key, notes)
    note_number = 0
    major_scale = []

    while note_number < len(organized_on_key):
        if note_number == 0:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 2:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 4:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 5:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 7:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 9:
            major_scale.append(organized_on_key[note_number])

        elif note_number == 11:
            major_scale.append(organized_on_key[note_number])

        note_number = note_number + 1

    return major_scale
