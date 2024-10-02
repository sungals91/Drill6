import random
from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')
running = True
x, y = 800//2, 600//2

def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
    pass

while running:
    clear_canvas()
    background.draw(x, y)
    update_canvas()
    handle_events()

close_canvas()