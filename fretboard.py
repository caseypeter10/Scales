import scl
def fretboard(tunings, key):
    fretboard = []
    # takes in a list of tunings and then strings are generated from those tunings
    # using the string prep function and appending the result of each string creation
    # to the list fretboard
    for i in tunings:
        fretboard.append(scl.string_prep(i, scl.note_filter(key)))

    return fretboard
