def on_button_pressed_a():
    ciocan1.change(LedSpriteProperty.X, -1)
    ciocan2.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ciocan1, ciocan2
    ciocan1.change(LedSpriteProperty.Y, 2)
    ciocan2.change(LedSpriteProperty.Y, 2)
    if ciocan2.is_touching(bila):
        game.add_score(1)
        basic.show_number(game.score())
    basic.pause(500)
    ciocan1.delete()
    ciocan2.delete()
    ciocan1 = game.create_sprite(2, 1)
    ciocan2 = game.create_sprite(2, 2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    ciocan1.change(LedSpriteProperty.X, 1)
    ciocan2.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

ciocan2: game.LedSprite = None
ciocan1: game.LedSprite = None
bila: game.LedSprite = None
score = 0
bila = game.create_sprite(randint(0, 4), 4)
ciocan1 = game.create_sprite(2, 1)
ciocan2 = game.create_sprite(2, 2)
timp_pornire = input.running_time()

def on_forever():
    global bila
    basic.pause(2000)
    bila.delete()
    bila = game.create_sprite(randint(0, 4), 4)
basic.forever(on_forever)

def on_forever2():
    if input.running_time() - timp_pornire >= 20000:
        game.game_over()
basic.forever(on_forever2)
