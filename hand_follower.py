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
    clear_canvas()
    background.draw(400, 300)
    random_x, random_y = random_coordinate()
    arrow.draw(random_x, random_y)
    update_canvas()
    handle_events()

    for i in range(0, 100+1, 5):
        clear_canvas()
        background.draw(400, 300)
        arrow.draw(random_x, random_y)

        t = i / 100
        char_x = (1-t) * x + t * random_x
        char_y = (1-t) * y + t * random_y
        if x > random_x:
            character.clip_draw(frame * 100, 0, 100, 100, char_x, char_y)
        else:
            character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', char_x, char_y, 100, 100)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.03)
        x,y = char_x, char_y

close_canvas()