import scl
def scale_on_board(scale, fretboard):
    # adds a * to list values that are also in the scale

    for string_index, string in enumerate(fretboard):
        for fret, pitch in enumerate(string):
            if pitch in scale:
                fretboard[string_index][fret] += 'v'

    return fretboard
