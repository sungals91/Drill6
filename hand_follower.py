import random
from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')
running = True
x, y = 800//2, 600//2
background_width, background_height = 800, 600
arrow_width, arrow_height = 50, 52

def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def random_arrow_draw():
    arrow_x = random.randint(arrow_width//2, background_width - arrow_width//2)
    arrow_y = random.randint(arrow_height//2, background_height - arrow_height//2)
    arrow.draw(arrow_x,arrow_y)
    pass

while running:
    clear_canvas()
    background.draw(x, y)
    random_arrow_draw()
    update_canvas()
    handle_events()
    delay(1)

close_canvas()