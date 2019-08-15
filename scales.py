from PIL import Image, ImageDraw, ImageFont
import numpy

def note_filter(key):
    if key in ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']:

        return ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', ]

    else:

        return ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


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


def scale_finder(key, notes):
    # generates major_scale based on filtering a list returned by the string_prep
    # function

    organized_on_key = string_prep(key, notes)
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


def fretboard(tunings, key):
    fretboard = []
    # takes in a list of tunings and then strings are generated from those tunings
    # using the string prep function and appending the result of each string creation
    # to the list fretboard
    for i in tunings:
        fretboard.append(string_prep(i, note_filter(key)))

    return fretboard


def fretboard_printer(fretboard):
    # formats the printing of the fretboard nicely
    print(type(fretboard))
    print(type(fretboard))
    for i in fretboard:
        print(i)
    return


def scale_on_board(scale, fretboard):
    # adds a * to list values that are also in the scale

    for string_index, string in enumerate(fretboard):
        for fret, pitch in enumerate(string):
            if pitch in scale:
                fretboard[string_index][fret] += 'v'

    return fretboard

def c_major_test():
    standard_fretboard = fretboard(['F', 'A#', 'D#', 'G#', 'C', 'F'], 'C')
    fretboard_w_scale = scale_on_board(scale_finder('C', note_filter('C')), standard_fretboard)
    fretboard_w_scale.reverse()
    fretboard_printer(fretboard_w_scale)

    draw_board()
    return


standard_fretboard = fretboard(['F', 'A#', 'D#', 'G#', 'C', 'F'], 'C')
#std_ftbd =

# print standard_fretboard
# print scale_finder('B',note_filter('B'))


# print string_prep('C',note_filter('C'))
# print note_filter('C')
# print standard_fretboard
fretboard_w_scale = scale_on_board(scale_finder('C', note_filter('C')), standard_fretboard)
fretboard_w_scale.reverse()

fretboard_printer(fretboard_w_scale)

#prepping fonts
sans12 = ImageFont.truetype(font_path, 12)
font = sans12
note_fill = 'yellow'

def draw_board(width=1100,height=200, board=fretboard_w_scale):

    #prepping fonts
    font_path = "C:/Users/Peter/Documents/R/win-library/3.5/hrbrthemes/fonts/plex-sans/IBMPlexSans-Bold.ttf"
    sans12 = ImageFont.truetype(font_path, 12)
    font = sans12
    note_fill = 'yellow'


    img = Image.new('RGB',(width,height),color='white')
    draw = ImageDraw.Draw(img)

    init_fret_dis = 165
    current_fret_dis = init_fret_dis
    fret_distance_list = []
    cumulative_distance_list = [0]
    fret_mid_list = []
    cumulative_dist = 0
    act_fret_list = []

    # drawing frets
    for i in range(13):
        if 0 == 0:
            print('drawing frets')
            print([(i*current_fret_dis + (init_fret_dis/2),0),(i*current_fret_dis + (init_fret_dis/2),height)])

            act_fret_x = (i*current_fret_dis + (init_fret_dis/2))
            act_fret_list.append(act_fret_x)

            draw.line([(act_fret_x,0),(act_fret_x,height)], fill=0, width= 7)
            #draw.line([(cumulative_distance_list[i],0),(cumulative_distance_list[i],200)], fill=0, width= 7)
            fret_distance_list.append(current_fret_dis)
            current_fret_dis *= 1/(pow(2,(1/12)))

    # drawing strings
    print("current_fret_dis", current_fret_dis)

    for i in range(6):
        draw.line([(0,i*(height/6)+(height/12)),(width,i*(height/6)+(height/12))], fill=0, width=i + 1)

    for i in range(len(fret_distance_list)):
        print(fret_distance_list[i])
        cumulative_dist += fret_distance_list[i]
        cumulative_distance_list.append(cumulative_dist)

    midpoint_list = []
    #Calculating midpoints of each fret
    for i in range(len(act_fret_list)):
        try:
            midpoint = (act_fret_list[i] + act_fret_list[i+1])/2
            midpoint_list.append(midpoint)
        except:
            print("end of list")

    print("cumulative_distance_list ",cumulative_distance_list)
    print("midpoint list", midpoint_list)

    #img = img.transpose(Image.FLIP_LEFT_RIGHT)
    #img = img.transpose(Image.FLIP_TOP_BOTTOM)

    #Drawing circles at midpoints of each fret and string
    #Length of board is 6 for a standard guitar

    #iterating all strings in the board
    for i in range(len(board)):
        string_y = i*(height/6)+(height/12)
        #iterating through all frets in a string
        for j in range(len(midpoint_list)):
            print("circle")
            top_left_bound = (midpoint_list[j]-10, string_y-10)
            print(top_left_bound)
            bottom_right_bound = (midpoint_list[j]+10, string_y+10)
            print(bottom_right_bound)
            print(board[i][j])
            print('v' in board[i][j])
            if 'v' in board[i][j]:
                draw.ellipse((top_left_bound, bottom_right_bound), fill=(100, 0, 0), outline=(80, 0, 10), width=3)

                if '#' in board[i][j]:
                    draw.text((midpoint_list[j]-5,string_y-7), board[i][j][:2], fill=note_fill, font=font)

                else:
                    draw.text((midpoint_list[j] - 5, string_y - 7), board[i][j][:1], fill=note_fill, font=font)

            else:
                draw.ellipse((top_left_bound,bottom_right_bound),fill=(100,100,100),outline=(80,80,90),width=3)
                draw.text((midpoint_list[j]-5, string_y-7), board[i][j], fill=note_fill, font=font)

    img.show()

draw_board()
