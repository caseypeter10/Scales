import scl
def c_major_test():
    standard_fretboard = scl.fretboard(['F', 'A#', 'D#', 'G#', 'C', 'F'], 'C')
    fretboard_w_scale = scl.scale_on_board(scl.scale_finder('C', scl.note_filter('C')), standard_fretboard)
    fretboard_w_scale.reverse()
    scl.fretboard_printer(fretboard_w_scale)

    scl.draw_board()
    return
