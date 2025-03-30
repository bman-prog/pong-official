plate_left = sprites.create(img("""
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
"""), SpriteKind.player)


plate_right = sprites.create(img("""
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
    . . 8 8 8 . .
"""), SpriteKind.player)

plate_left.set_position(10, 60)
plate_right.set_position(150, 60)
plate_left.set_stay_in_screen(True)
plate_right.set_stay_in_screen(True)


controller.move_sprite(plate_right, 0, 195)


def move_left_paddle():
    if controller.B.is_pressed():
        plate_left.y -= 4.1
    elif controller.A.is_pressed():
        plate_left.y += 4.1

game.on_update(move_left_paddle)
