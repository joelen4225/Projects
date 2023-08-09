# Joe Leonard and Abram Johan - CS1111

# Game Idea: UVA Pacman
# The game will run the same as Pacman with two working levels. They will differ in layout and difficulty. The first
# level will be easier and the sprites will move at a slower pace compared to those in level two.

# Five Required Features
# 1. The controlled sprite is able to move up, down, right and left.
#  - Fulfilled using the 'pygame.KEY_##' functions.
# 2. The four uncontrolled sprites move in a randomized direction at a certain speed.
#  - Fulfilled using the 'random()' function with a combination of the Pygame's movement functions.
# 3. The uncontrolled sprites leave a certain place at a certain direction.
#  - Fulfilled using direction and speed variables we will create.
# 4. The uncontrolled sprites will change color and move away from the controlled sprite after the specific item is passed.
#  - Fulfilled using a defined function to invert the colors and flip the direction of the uncontrolled sprite.
# 5. A live health bar in the corner portion of the screen that terminates the game once three lives have been used.
#  - Fulfilled by detecting collision of uncontrolled and controlled sprites along with ending the game, but starting
#    the screen from where the player left off.

# Four Optional Features
# 1. The controlled sprite is a circular UVA logo and the uncontrolled sprites are square logos of UVA rivals.
#  - Fulfilled using 'pygame.image' functions and editing the pictures before hand.
# 2. The uncontrolled sprites move at a faster pace making it more difficult for the player.
#  - Made using varying speeds in both the X and Y direction.
# 3. Flip between the screen at the sides.
#  - Using detection of hitting an invisible wall or other specific place.
# 4. A score counter in the top portion of the screen that counts how many times the sprite passes a specific item.
#  - Fulfilled by detection collision of the controlled sprite and the specified item then adding one to a certain
#    score variable.

# Import Libraries
import pygame
import gamebox
import random


# Start Variables
camera = gamebox.Camera(800, 600)
game_on = False
attack = False
score_counter = 0
life_counter = 2
gen_counter = 0

# Text Variables
start_text = gamebox.from_text(400, 356, "Start Game", 50, "black", bold=True)
start_text_caption = gamebox.from_text(400, 383, "Click Space to Start and Use Arrows to Move", 33, "black", bold=True)
score_text = gamebox.from_text(100, 19, "Score:", 25, "red", bold=True)
score_count_text = gamebox.from_text(140, 19, str(score_counter), 25, "red", bold=True)
lives_text = gamebox.from_text(185, 19, "Lives:", 25, "red", bold=True)
heart1 = gamebox.from_image(230, 19, 'heart_icon.png')
heart2 = gamebox.from_image(255, 19, 'heart_icon.png')
heart3 = gamebox.from_image(280, 19, 'heart_icon.png')
name_text_right = gamebox.from_text(600, 300, "Abram Johan", 20, "black", bold=True)
comp_id_right = gamebox.from_text(600, 320, "atd2ec", 20, "black", bold=True)
name_text_left = gamebox.from_text(200, 300, "Joe Leonard", 20, "black", bold=True)
comp_id_left = gamebox.from_text(200, 320, "ymd3tv", 20, "black", bold=True)
num = random.randint(1, 2)
new_num = random.randint(1, 2)

# Life List
lives = [heart1, heart2, heart3]

# Outside Walls Variables
top_horiz = gamebox.from_color(0, 0, "orange", 1600, 15)
bottom_horiz = gamebox.from_color(800, 600, "orange", 1600, 15)
top_left_vert = gamebox.from_color(0, 0, "orange", 15, 445)
bottom_left_vert = gamebox.from_color(0, 600, "orange", 15, 445)
top_right_vert = gamebox.from_color(800, 0, "orange", 15, 445)
bottom_right_vert = gamebox.from_color(800, 600, "orange", 15, 445)
top_left_in = gamebox.from_color(0, 225, "orange", 160, 10)
top_left_down = gamebox.from_color(75, 250, "orange", 10, 60)
top_left_out = gamebox.from_color(0, 283, "orange", 160, 10)
top_right_in = gamebox.from_color(800, 225, "orange", 160, 10)
top_right_down = gamebox.from_color(724, 253, "orange", 10, 60)
top_right_out = gamebox.from_color(800, 280, "orange", 160, 10)
bottom_left_in = gamebox.from_color(0, 375, "orange", 160, 10)
bottom_left_up = gamebox.from_color(75, 350, "orange", 10, 60)
bottom_left_out = gamebox.from_color(0, 325, "orange", 160, 10)
bottom_right_in = gamebox.from_color(800, 375, "orange", 160, 10)
bottom_right_up = gamebox.from_color(724.5, 350, "orange", 10, 57)
bottom_right_out = gamebox.from_color(800, 325, "orange", 160, 10)
right_flip = gamebox.from_color(800, 303, "midnightblue", 15, 35.5)
left_flip = gamebox.from_color(0, 304.5, "midnightblue", 15, 32)

# Outside Walls List
out_walls = [top_horiz, bottom_horiz, top_left_vert, bottom_left_vert, top_right_vert, bottom_right_vert, top_left_in,
             top_left_down, top_left_out, top_right_in, top_right_down, top_right_out, bottom_left_in, bottom_left_up,
             bottom_left_out, bottom_right_in, bottom_right_up, bottom_right_out]

# Inside Walls Variables
top_left_1 = gamebox.from_color(170, 75, "orange", 200, 10)
top_left_2 = gamebox.from_color(65, 100, "orange", 10, 60)
top_middle_1 = gamebox.from_color(400, 140, "orange", 550, 10)
top_middle_2 = gamebox.from_color(400, 30, "orange", 10, 130)
top_right_1 = gamebox.from_color(630, 75, "orange", 200, 10)
top_right_2 = gamebox.from_color(735, 100, "orange", 10, 60)
middle_top_right = gamebox.from_color(200, 185, "orange", 280, 10)
middle_right = gamebox.from_color(200, 300, "orange", 110, 230)
middle_top_left = gamebox.from_color(600, 185, "orange", 280, 10)
middle_left = gamebox.from_color(600, 300, "orange", 110, 230)
bottom_middle = gamebox.from_color(400, 475, "orange", 600, 10)
bottom_left = gamebox.from_color(100, 508, "orange", 10, 75)
bottom_middle_down = gamebox.from_color(400, 508, "orange", 10, 75)
bottom_right = gamebox.from_color(700, 508, "orange", 10, 75)
bottom_left_up = gamebox.from_color(250, 562.5, "orange", 10, 75)
bottom_right_up = gamebox.from_color(550, 562.5, "orange", 10, 75)

# Inside Walls List
ins_walls = [top_left_1, top_left_2, top_middle_1, top_middle_2, top_right_1, top_right_2,
             middle_top_right, middle_right, middle_top_left, middle_left,
             bottom_middle, bottom_left, bottom_middle_down, bottom_right, bottom_left_up, bottom_right_up]

# Cage Variables
bottom_cage = gamebox.from_color(400, 325, "orange", 120, 15)
top_cage_orange_1 = gamebox.from_color(360, 270, "orange", 40, 15)
top_cage_orange_2 = gamebox.from_color(440, 270, "orange", 40, 15)
top_cage_white = gamebox.from_color(400, 270, "midnightblue", 40, 15)
right_cage = gamebox.from_color(460, 297.7, "orange", 15, 70)
left_cage = gamebox.from_color(340, 297.7, "orange", 15, 70)

# Cage List
cages = [bottom_cage, top_cage_orange_1, top_cage_orange_2, right_cage, left_cage]

# Icon Variables
uva_logo = gamebox.from_circle(400, 410, "orange", 15)
unc_logo = gamebox.from_circle(35, 40, "dodgerblue", 15)
duke_logo = gamebox.from_circle(765, 40, "blue", 15)
louis_logo = gamebox.from_circle(35, 570, "red", 15)
vtech_logo = gamebox.from_circle(760, 570, "maroon", 15)
top_right_prize = gamebox.from_circle(760, 35, "gold", 15)
top_left_prize = gamebox.from_circle(40, 35, "gold", 15)
bottom_right_prize = gamebox.from_circle(760, 565, "gold", 15)
bottom_left_prize = gamebox.from_circle(40, 565, "gold", 15)
uva = gamebox.from_image(400, 410, "uvalogo_25x25.png")
vt = gamebox.from_image(760, 570,"vt pic 25.png")
louis = gamebox.from_image(35, 570, "louis 25 pic.jpg")
duke = gamebox.from_image(765, 40, 'duke pic 25.jpg')
unc = gamebox.from_image(35, 40, 'unc_pic_25x25.png')


# Logo List
logos = [uva_logo, unc_logo, duke_logo, louis_logo, vtech_logo, uva, vt, louis, duke, unc]
enemy = [unc_logo, duke_logo, louis_logo, vtech_logo]

#Initializing Speed
vtspeedx = 0
vtspeedy = 0
dukespeedx = 0
dukespeedy = 0
uncspeedx = 0
uncspeedy = 0
louisspeedx = 0
louisspeedy = 0

# Prize List
prizes = [top_right_prize, top_left_prize, bottom_right_prize, bottom_left_prize]

# Coin Variables
coin_1 = gamebox.from_circle(400, 117, "gold", 8)
coin_2 = gamebox.from_circle(360, 117, "gold", 8)
coin_3 = gamebox.from_circle(320, 117, "gold", 8)
coin_4 = gamebox.from_circle(280, 117, "gold", 8)
coin_5 = gamebox.from_circle(240, 117, "gold", 8)
coin_6 = gamebox.from_circle(200, 117, "gold", 8)
coin_7 = gamebox.from_circle(160, 117, "gold", 8)
coin_8 = gamebox.from_circle(120, 117, "gold", 8)
coin_9 = gamebox.from_circle(440, 117, "gold", 8)
coin_10 = gamebox.from_circle(480, 117, "gold", 8)
coin_11 = gamebox.from_circle(520, 117, "gold", 8)
coin_12 = gamebox.from_circle(560, 117, "gold", 8)
coin_13 = gamebox.from_circle(600, 117, "gold", 8)
coin_14 = gamebox.from_circle(640, 117, "gold", 8)
coin_15 = gamebox.from_circle(680, 117, "gold", 8)
coin_16 = gamebox.from_circle(400, 165, "gold", 8)
coin_17 = gamebox.from_circle(360, 165, "gold", 8)
coin_18 = gamebox.from_circle(320, 165, "gold", 8)
coin_19 = gamebox.from_circle(280, 165, "gold", 8)
coin_20 = gamebox.from_circle(240, 165, "gold", 8)
coin_21 = gamebox.from_circle(200, 165, "gold", 8)
coin_22 = gamebox.from_circle(160, 165, "gold", 8)
coin_23 = gamebox.from_circle(120, 165, "gold", 8)
coin_24 = gamebox.from_circle(80, 165, "gold", 8)
coin_25 = gamebox.from_circle(40, 165, "gold", 8)
coin_26 = gamebox.from_circle(440, 165, "gold", 8)
coin_27 = gamebox.from_circle(480, 165, "gold", 8)
coin_28 = gamebox.from_circle(520, 165, "gold", 8)
coin_29 = gamebox.from_circle(560, 165, "gold", 8)
coin_30 = gamebox.from_circle(600, 165, "gold", 8)
coin_31 = gamebox.from_circle(640, 165, "gold", 8)
coin_32 = gamebox.from_circle(680, 165, "gold", 8)
coin_33 = gamebox.from_circle(720, 165, "gold", 8)
coin_34 = gamebox.from_circle(760, 165, "gold", 8)
coin_35 = gamebox.from_circle(760, 125, "gold", 8)
coin_36 = gamebox.from_circle(760, 85, "gold", 8)
coin_37 = gamebox.from_circle(40, 125, "gold", 8)
coin_38 = gamebox.from_circle(40, 85, "gold", 8)
coin_39 = gamebox.from_circle(40, 205, "gold", 8)
coin_40 = gamebox.from_circle(760, 205, "gold", 8)
coin_41 = gamebox.from_circle(80, 205, "gold", 8)
coin_42 = gamebox.from_circle(120, 205, "gold", 8)
coin_43 = gamebox.from_circle(720, 205, "gold", 8)
coin_44 = gamebox.from_circle(680, 205, "gold", 8)
coin_45 = gamebox.from_circle(680, 245, "gold", 8)
coin_46 = gamebox.from_circle(680, 285, "gold", 8)
coin_47 = gamebox.from_circle(120, 245, "gold", 8)
coin_48 = gamebox.from_circle(120, 285, "gold", 8)
coin_49 = gamebox.from_circle(400, 205, "gold", 8)
coin_50 = gamebox.from_circle(400, 205, "gold", 8)
coin_51 = gamebox.from_circle(360, 205, "gold", 8)
coin_52 = gamebox.from_circle(320, 205, "gold", 8)
coin_53 = gamebox.from_circle(280, 205, "gold", 8)
coin_54 = gamebox.from_circle(440, 205, "gold", 8)
coin_55 = gamebox.from_circle(480, 205, "gold", 8)
coin_56 = gamebox.from_circle(520, 205, "gold", 8)
coin_57 = gamebox.from_circle(520, 245, "gold", 8)
coin_58 = gamebox.from_circle(520, 285, "gold", 8)
coin_59 = gamebox.from_circle(520, 325, "gold", 8)
coin_60 = gamebox.from_circle(520, 365, "gold", 8)
coin_61 = gamebox.from_circle(520, 405, "gold", 8)
coin_62 = gamebox.from_circle(520, 445, "gold", 8)
coin_63 = gamebox.from_circle(280, 205, "gold", 8)
coin_64 = gamebox.from_circle(280, 245, "gold", 8)
coin_65 = gamebox.from_circle(280, 285, "gold", 8)
coin_66 = gamebox.from_circle(280, 325, "gold", 8)
coin_67 = gamebox.from_circle(280, 365, "gold", 8)
coin_68 = gamebox.from_circle(280, 405, "gold", 8)
coin_69 = gamebox.from_circle(280, 445, "gold", 8)
coin_70 = gamebox.from_circle(120, 325, "gold", 8)
coin_71 = gamebox.from_circle(120, 365, "gold", 8)
coin_72 = gamebox.from_circle(120, 405, "gold", 8)
coin_73 = gamebox.from_circle(120, 445, "gold", 8)
coin_74 = gamebox.from_circle(680, 325, "gold", 8)
coin_75 = gamebox.from_circle(680, 365, "gold", 8)
coin_76 = gamebox.from_circle(680, 405, "gold", 8)
coin_77 = gamebox.from_circle(680, 445, "gold", 8)
coin_78 = gamebox.from_circle(400, 445, "gold", 8)
coin_79 = gamebox.from_circle(360, 445, "gold", 8)
coin_80 = gamebox.from_circle(320, 445, "gold", 8)
coin_81 = gamebox.from_circle(240, 445, "gold", 8)
coin_82 = gamebox.from_circle(200, 445, "gold", 8)
coin_83 = gamebox.from_circle(160, 445, "gold", 8)
coin_84 = gamebox.from_circle(80, 445, "gold", 8)
coin_85 = gamebox.from_circle(40, 445, "gold", 8)
coin_86 = gamebox.from_circle(440, 445, "gold", 8)
coin_87 = gamebox.from_circle(480, 445, "gold", 8)
coin_88 = gamebox.from_circle(560, 445, "gold", 8)
coin_89 = gamebox.from_circle(600, 445, "gold", 8)
coin_90 = gamebox.from_circle(640, 445, "gold", 8)
coin_91 = gamebox.from_circle(720, 445, "gold", 8)
coin_92 = gamebox.from_circle(760, 445, "gold", 8)
coin_93 = gamebox.from_circle(720, 405, "gold", 8)
coin_94 = gamebox.from_circle(760, 405, "gold", 8)
coin_95 = gamebox.from_circle(80, 405, "gold", 8)
coin_96 = gamebox.from_circle(40, 405, "gold", 8)
coin_97 = gamebox.from_circle(40, 485, "gold", 8)
coin_98 = gamebox.from_circle(40, 525, "gold", 8)
coin_99 = gamebox.from_circle(760, 485, "gold", 8)
coin_100 = gamebox.from_circle(760, 525, "gold", 8)
coin_101 = gamebox.from_circle(80, 565, "gold", 8)
coin_102 = gamebox.from_circle(120, 565, "gold", 8)
coin_103 = gamebox.from_circle(160, 565, "gold", 8)
coin_104 = gamebox.from_circle(200, 565, "gold", 8)
coin_105 = gamebox.from_circle(200, 535, "gold", 8)
coin_106 = gamebox.from_circle(200, 505, "gold", 8)
coin_107 = gamebox.from_circle(250, 505, "gold", 8)
coin_108 = gamebox.from_circle(300, 505, "gold", 8)
coin_109 = gamebox.from_circle(300, 535, "gold", 8)
coin_110 = gamebox.from_circle(300, 565, "gold", 8)
coin_111 = gamebox.from_circle(340, 565, "gold", 8)
coin_112 = gamebox.from_circle(380, 565, "gold", 8)
coin_113 = gamebox.from_circle(420, 565, "gold", 8)
coin_114 = gamebox.from_circle(460, 565, "gold", 8)
coin_115 = gamebox.from_circle(500, 565, "gold", 8)
coin_116 = gamebox.from_circle(500, 535, "gold", 8)
coin_117 = gamebox.from_circle(500, 505, "gold", 8)
coin_118 = gamebox.from_circle(550, 505, "gold", 8)
coin_119 = gamebox.from_circle(600, 505, "gold", 8)
coin_120 = gamebox.from_circle(600, 535, "gold", 8)
coin_121 = gamebox.from_circle(600, 565, "gold", 8)
coin_122 = gamebox.from_circle(640, 565, "gold", 8)
coin_123 = gamebox.from_circle(680, 565, "gold", 8)
coin_124 = gamebox.from_circle(720, 565, "gold", 8)
coin_125 = gamebox.from_circle(440, 77, "gold", 8)
coin_126 = gamebox.from_circle(360, 77, "gold", 8)
coin_127 = gamebox.from_circle(360, 37, "gold", 8)
coin_128 = gamebox.from_circle(320, 37, "gold", 8)
coin_129 = gamebox.from_circle(280, 37, "gold", 8)
coin_130 = gamebox.from_circle(240, 37, "gold", 8)
coin_131 = gamebox.from_circle(200, 37, "gold", 8)
coin_132 = gamebox.from_circle(160, 37, "gold", 8)
coin_133 = gamebox.from_circle(120, 37, "gold", 8)
coin_134 = gamebox.from_circle(80, 37, "gold", 8)
coin_135 = gamebox.from_circle(440, 37, "gold", 8)
coin_136 = gamebox.from_circle(480, 37, "gold", 8)
coin_137 = gamebox.from_circle(520, 37, "gold", 8)
coin_138 = gamebox.from_circle(560, 37, "gold", 8)
coin_139 = gamebox.from_circle(600, 37, "gold", 8)
coin_140 = gamebox.from_circle(640, 37, "gold", 8)
coin_141 = gamebox.from_circle(680, 37, "gold", 8)
coin_142 = gamebox.from_circle(720, 37, "gold", 8)


# coin List
coins = [coin_1, coin_2, coin_3, coin_4, coin_5, coin_6, coin_7, coin_8, coin_9, coin_10, coin_11, coin_12, coin_13,
         coin_14, coin_15, coin_16, coin_17, coin_18, coin_19, coin_20, coin_21, coin_22, coin_23, coin_24, coin_25,
         coin_26, coin_27, coin_28, coin_29, coin_30, coin_31, coin_32, coin_33, coin_34, coin_35, coin_36, coin_37,
         coin_38, coin_39, coin_40, coin_41, coin_42, coin_43, coin_44, coin_45, coin_46, coin_47, coin_48, coin_49,
         coin_50, coin_51, coin_52, coin_53, coin_54, coin_55, coin_56, coin_57, coin_58, coin_59, coin_60, coin_61,
         coin_62, coin_63, coin_64, coin_65, coin_66, coin_67, coin_68, coin_69, coin_70, coin_71, coin_72, coin_73,
         coin_74, coin_75, coin_76, coin_77, coin_78, coin_79, coin_80, coin_81, coin_82, coin_83, coin_84, coin_85,
         coin_86, coin_87, coin_88, coin_89, coin_90, coin_91, coin_92, coin_93, coin_94, coin_95, coin_96, coin_97,
         coin_98, coin_99, coin_100, coin_101, coin_102, coin_103, coin_104, coin_105, coin_106, coin_107, coin_108,
         coin_109, coin_110, coin_111, coin_112, coin_113, coin_114, coin_115, coin_116, coin_117, coin_118, coin_119,
         coin_120, coin_121, coin_122, coin_123, coin_124, coin_125, coin_126, coin_127, coin_128, coin_129, coin_130,
         coin_131, coin_132, coin_133, coin_134, coin_135, coin_136, coin_137, coin_138, coin_139, coin_140, coin_141,
         coin_142]

#Game Over Screen
game_over = gamebox.from_text(400, 300, "Game Over", 100, "black")

def tick(keys):
    global game_on, camera, score_counter, life_counter, time_counter, start_text, start_text_caption, out_walls, ins_walls, \
    right_flip, left_flip, cages, logos, prizes, score_text, score_count_text, lives_text, lives_count_text, life_counter, \
    score_counter, coins, top_cage_white, num, vtspeedx, vtspeedy, dukespeedx, dukespeedy, uncspeedx, uncspeedy, louisspeedx, louisspeedy, \
    gen_counter, game_over, uva_logo, unc_logo, duke_logo, louis_logo, vtech_logo, attack, name_text_right, comp_id_right, \
    name_text_left, comp_id_left, uva, duke, louis, unc, vt, lives

    # Initializing the Screen's View
    camera.clear("midnightblue")
    for coin in coins:
        camera.draw(coin)
    camera.draw(score_text)
    camera.draw(score_count_text)
    camera.draw(lives_text)
    for live in lives:
        camera.draw(live)
    for wall in out_walls:
        camera.draw(wall)
    for wall in ins_walls:
        camera.draw(wall)
    for cage in cages:
        camera.draw(cage)
    camera.draw(right_flip)
    camera.draw(left_flip)
    for prize in prizes:
        camera.draw(prize)
    for logo in logos:
        camera.draw(logo)
    camera.draw(start_text)
    camera.draw(start_text_caption)
    camera.draw(name_text_right)
    camera.draw(comp_id_right)
    camera.draw(name_text_left)
    camera.draw(comp_id_left)

    #Changing the Enemy Logos
    unc_logo.color = "dodgerblue"
    duke_logo.color = "blue"
    louis_logo.color = "red"
    vtech_logo.color = "maroon"

    #User Interaction
    camera.display()
    if pygame.K_SPACE in keys:
        game_on = True

    #Main Code
    if game_on == True:
        start_text = gamebox.from_text(1000, 475, "Start Game", 50, "midnightblue", bold=True)
        start_text_caption = gamebox.from_text(1000, 500, "Click Space", 35, "midnightblue", bold=True)
        name_text_right = gamebox.from_text(600, 300, "Abram Johan", 20, "orange", bold=True)
        comp_id_right = gamebox.from_text(600, 320, "atd2ec", 20, "orange", bold=True)
        name_text_left = gamebox.from_text(200, 300, "Joe Leonard", 20, "orange", bold=True)
        comp_id_left = gamebox.from_text(200, 320, "ymd3tv", 20, "orange", bold=True)
        camera.display()

        uva.x = uva_logo.x
        uva.y = uva_logo.y
        duke.x = duke_logo.x
        duke.y = duke_logo.y
        louis.x = louis_logo.x
        louis.y = louis_logo.y
        unc.x = unc_logo.x
        unc.y = unc_logo.y
        vt.y = vtech_logo.y
        vt.x = vtech_logo.x

        # Code Used for Random Movement From Enemies
        for logo in enemy:
            if logo.x == 35 and logo.y == 40:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
            if logo.x == 35 and logo.y == 40:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # down, right
            elif logo.x == 360 and logo.y == 40:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # down, left
            elif logo.x == 360 and logo.y == 115:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # up, right, left
            elif logo.x == 100 and logo.y == 115:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # down, right
            elif logo.x == 100 and logo.y == 165:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # left, right, up
            elif logo.x == 35 and logo.y == 165:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # up, right, down
            elif logo.x == 35 and logo.y == 205:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = -1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = -1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = -1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = -1
                # up, right
            elif logo.x == 120 and logo.y == 205:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # left, down
            elif logo.x == 120 and logo.y == 445:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # up, left, right
            elif logo.x == 35 and logo.y == 445:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # right, down
            elif logo.x == 35 and logo.y == 570:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = -1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = -1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = -1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = -1
                # up, right
            elif logo.x == 200 and logo.y == 570:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = -1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = -1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = -1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = -1
                # up, left
            elif logo.x == 200 and logo.y == 500:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # down, right
            elif logo.x == 300 and logo.y == 500:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # left, down
            elif logo.x == 300 and logo.y == 570:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = -1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = -1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = -1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = -1
                # right, up
            elif logo.x == 500 and logo.y == 570:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = -1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = -1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = -1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = -1
                # up, left
            elif logo.x == 500 and logo.y == 500:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # right, down
            elif logo.x == 600 and logo.y == 500:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # down, left
            elif logo.x == 600 and logo.y == 570:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = -1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = -1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = -1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = -1
                # up, right
            elif logo.x == 760 and logo.y == 570:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = -1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = -1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = -1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = -1
                # up, left
            elif logo.x == 760 and logo.y == 445:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # left, down
            elif logo.x == 680 and logo.y == 445:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # up, right, left
            elif logo.x == 680 and logo.y == 205:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # right, down
            elif logo.x == 765 and logo.y == 205:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = -1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = -1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = -1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = -1
                # left, up
            elif logo.x == 765 and logo.y == 165:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 0
                        vtspeedy = 1
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 0
                        uncspeedy = 1
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 0
                        dukespeedy = 1
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 0
                        louisspeedy = 1
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # up, left, down
            elif logo.x == 765 and logo.y == 40:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # left, down
            elif logo.x == 440 and logo.y == 40:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # right, down
            elif logo.x == 440 and logo.y == 115:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # left, right, up
            elif logo.x == 700 and logo.y == 115:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # left, down
            elif logo.x == 700 and logo.y == 165:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # left, right, up
            elif logo.x == 400 and logo.y == 165:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = 1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = 1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = 1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = 1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # left, right, down
            elif logo.x == 400 and logo.y == 210:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # left, right, up
            elif logo.x == 280 and logo.y == 210:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # down, right
            elif logo.x == 280 and logo.y == 445:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # up, right, left
            elif logo.x == 520 and logo.y == 445:
                if logo == vtech_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        vtspeedx = 1
                        vtspeedy = 0
                    elif direction == 2:
                        vtspeedx = 0
                        vtspeedy = -1
                    else:
                        vtspeedx = -1
                        vtspeedy = 0
                if logo == unc_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        uncspeedx = 1
                        uncspeedy = 0
                    elif direction == 2:
                        uncspeedx = 0
                        uncspeedy = -1
                    else:
                        uncspeedx = -1
                        uncspeedy = 0
                if logo == duke_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        dukespeedx = 1
                        dukespeedy = 0
                    elif direction == 2:
                        dukespeedx = 0
                        dukespeedy = -1
                    else:
                        dukespeedx = -1
                        dukespeedy = 0
                if logo == louis_logo:
                    direction = random.randint(1, 3)
                    if direction == 1:
                        louisspeedx = 1
                        louisspeedy = 0
                    elif direction == 2:
                        louisspeedx = 0
                        louisspeedy = -1
                    else:
                        louisspeedx = -1
                        louisspeedy = 0
                # up, right, left
            elif logo.x == 520 and logo.y == 210:
                if logo == vtech_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        vtspeedx = -1
                        vtspeedy = 0
                    else:
                        vtspeedx = 0
                        vtspeedy = 1
                elif logo == unc_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        uncspeedx = -1
                        uncspeedy = 0
                    else:
                        uncspeedx = 0
                        uncspeedy = 1
                elif logo == duke_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        dukespeedx = -1
                        dukespeedy = 0
                    else:
                        dukespeedx = 0
                        dukespeedy = 1
                elif logo == louis_logo:
                    direction = random.randint(1, 2)
                    if direction == 1:
                        louisspeedx = -1
                        louisspeedy = 0
                    else:
                        louisspeedx = 0
                        louisspeedy = 1
                # left, down

        #Changing the Speeds
        vtech_logo.x += vtspeedx * 5
        vtech_logo.y += vtspeedy * 5
        unc_logo.x += uncspeedx * 5
        unc_logo.y += uncspeedy * 5
        duke_logo.x += dukespeedx * 5
        duke_logo.y += dukespeedy * 5
        louis_logo.x += louisspeedx * 5
        louis_logo.y += louisspeedy * 5

        #Player Movement
        if pygame.K_RIGHT in keys:
            for logo in logos:
                if logo == uva_logo:
                    uva_logo.move(3, 0)
        if pygame.K_LEFT in keys:
            for logo in logos:
                if logo == uva_logo:
                    uva_logo.move(-3, 0)
        if pygame.K_UP in keys:
            for logo in logos:
                if logo == uva_logo:
                    uva_logo.move(0, -3)
        if pygame.K_DOWN in keys:
            for logo in logos:
                if logo == uva_logo:
                    uva_logo.move(0, 3)

        #Collision Detection With Walls
        for logo in logos:
            if logo.left_touches(left_flip):
                logo.move(770, 0)
            if logo.right_touches(right_flip):
                logo.move(-770, 0)
            for wall in out_walls:
                logo.move_to_stop_overlapping(wall)
            for cage in cages:
                logo.move_to_stop_overlapping(cage)
            for wall in ins_walls:
                logo.move_to_stop_overlapping(wall)

        #Collision Detection With Coins and Prizes
        for logo in logos:
            for coin in coins:
                if logo == uva_logo:
                    if logo.touches(coin):
                        score_counter += 1
                        score_count_text = gamebox.from_text(140, 20, str(score_counter), 25, "red", bold=True)
                        coins.remove(coin)
            for prize in prizes:
                if logo == uva_logo:
                    if logo.touches(prize):
                        score_counter += 2
                        score_count_text = gamebox.from_text(140, 20, str(score_counter), 25, "red", bold=True)
                        prizes.remove(prize)
                        attack = True

        #Normal User
        if attack == False:
            unc_logo.color = "dodgerblue"
            duke_logo.color = "blue"
            louis_logo.color = "red"
            vtech_logo.color = "maroon"
            for logo in logos:
                if logo == uva_logo:
                    for icon in enemy:
                        if logo.touches(icon):
                            life_counter -= 1
                            for i in range(len(lives)-(len(lives) - 1)):
                                lives.remove(lives[i])
                            for logo in logos:
                                if logo == uva_logo:
                                    logo.move(400-logo.x, 410-logo.y)
                                if logo == unc_logo:
                                    logo.move(35-logo.x, 40-logo.y)
                                if logo == duke_logo:
                                    logo.move(765-logo.x, 40-logo.y)
                                if logo == louis_logo:
                                    logo.move(35-logo.x, 570-logo.y)
                                if logo == vtech_logo:
                                    logo.move(760-logo.x, 570-logo.y)

        #When User Can Eat Enemies
        if attack == True:
            for logo in logos:
                if logo == uva_logo:
                    for logo_2 in logos:
                        if logo_2 != uva_logo and logo_2 != uva and logo_2 != vt and logo_2 != duke and logo_2 != unc and logo_2 != louis:
                            logo_2.color = "purple"
                            if logo.touches(logo_2):
                                if logo_2 == unc_logo or logo_2 == unc:
                                    logo_2.move(35-logo_2.x, 40-logo_2.y)
                                if logo_2 == duke_logo or logo_2 == duke:
                                    logo_2.move(765-logo_2.x, 40-logo_2.y)
                                if logo_2 == louis_logo or logo_2 == louis:
                                    logo_2.move(35-logo_2.x, 570-logo_2.y)
                                if logo_2 == vtech_logo or logo_2 == vt:
                                    logo_2.move(760-logo_2.x, 570-logo_2.y)
                                attack = False



        #Ends Game
        if life_counter < 0:
            game_on = False
            gen_counter = 2
            life_counter = 0

        #Ends Game
        if score_counter == 150:
            gen_counter = 2
            game_on = False


        camera.display()

    #End Game Display
    if game_on == False and gen_counter > 1:
        for logo_2 in logos:
            if logo_2 == uva_logo or logo_2 == uva:
                logo_2.move(400-logo_2.x, 410 - logo_2.y)
            if logo_2 == unc_logo or logo_2 == unc:
                logo_2.move(35 - logo_2.x, 40 - logo_2.y)
            if logo_2 == duke_logo or logo_2 == duke:
                logo_2.move(765 - logo_2.x, 40 - logo_2.y)
            if logo_2 == louis_logo or logo_2 == louis:
                logo_2.move(35 - logo_2.x, 570 - logo_2.y)
            if logo_2 == vtech_logo or logo_2 == vt:
                logo_2.move(760 - logo_2.x, 570 - logo_2.y)
        camera.draw(game_over)

    camera.display()




ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)