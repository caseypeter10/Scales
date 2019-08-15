import scl
from PIL import Image, ImageDraw, ImageFont

def draw_board(width=1100,height=200):

    font_path = "C:/Users/Peter/Documents/R/win-library/3.5/hrbrthemes/fonts/plex-sans/IBMPlexSans-Bold.ttf"
    sans12 = ImageFont.truetype(font_path, 12)
    font = sans12
    note_fill = 'yellow'


    standard_fretboard = scl.fretboard(['F', 'A#', 'D#', 'G#', 'C', 'F'], 'C')
    fretboard_w_scale = scl.scale_on_board(scl.scale_finder('C', scl.note_filter('C')), standard_fretboard)
    board = fretboard_w_scale

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
