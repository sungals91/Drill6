import random
from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')
running = True
x, y = 800//2, 600//2


while running:
    clear_canvas()
    background.draw(x, y)
    update_canvas()

close_canvas()