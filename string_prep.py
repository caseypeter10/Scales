def string_prep(start, notes):
    # This function is intended to provide an organized string of notes that can be used to generate the
    # note values for a guitar string
    prepared_notes = []
    note_counter = 0
    found_note = 0

    while note_counter < len(notes):

        if notes[note_counter] == start:

            found_note = note_counter  # records the location of the open string note in the raw note list

            while note_counter < len(notes):

                prepared_notes.append(notes[note_counter])

                # not sure where to up the note_counter seems to cause scale_on_board
                # to just return first note of each string
                note_counter = note_counter + 1
                if note_counter > 11:

                    # following if statement necessary for handling key of C
                    if start == 'C':
                        return prepared_notes
                    note_counter = 0  # starts over at beginning of notes

                elif note_counter == found_note:  # breaks out of prepared list creation

                    return prepared_notes
                # note_counter = note_counter + 1

        else:
            note_counter = note_counter + 1
