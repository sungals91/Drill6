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
frame = 0

def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def random_coordinate():
    rand_x = random.randint(arrow_width//2, background_width - arrow_width//2)
    rand_y = random.randint(arrow_height//2, background_height - arrow_height//2)
    return rand_x, rand_y

while running:
    random_x, random_y = random_coordinate()

    clear_canvas()
    background.draw(x, y)
    arrow.draw(random_x, random_y)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()